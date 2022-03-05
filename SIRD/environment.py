"""Module containing the enviroment class"""

import networkx as nx
import numpy as np
import random

from SIRD.agent import Agent
from SIRD.status import Status


class Environment:
    """Environment class representing a single simulation setting."""

    def __init__(self, beta, mu, mu_d, n_agents, n_init_infected, contact_network):
        self._beta = beta
        self._mu = mu
        self._mu_d = mu_d
        self._n_agents = n_agents
        self._network = self._generate_network(contact_network)
        self._agents = self._generate_agents(n_init_infected)

    def _generate_network(self, contact_network):
        """Returns adjacency matrix of network."""
        if contact_network == 'grid':
            if int(np.sqrt(self._n_agents)) ** 2 != self._n_agents:
                raise Exception('Only cubic numbers can be accepted! 2**2 = 4 usw.')
            network_dic = nx.grid_2d_graph(
                int(np.sqrt(self._n_agents)),
                int(np.sqrt(self._n_agents)),
                False
            )
            return nx.convert_matrix.to_numpy_array(network_dic, dtype=int)
        elif isinstance(contact_network, nx.Graph):
            if len(contact_network.nodes) != self._n_agents:
                raise Exception('Number of nodes and agents are different!')
            return nx.convert_matrix.to_numpy_array(contact_network, dtype=int)

    def _generate_agents(self, init_infected):
        """Returns list of agents."""

        agents = []
        for i in range(self._n_agents):
            if i < init_infected:
                agents.append(Agent(Status.INFECTED))
            else:
                agents.append(Agent(Status.SUSCEPTIBLE))
        return agents

    def _make_contact(self):
        """Determines if contact is infectious"""

        if random.randint(0, 100000) <= 100000 * self._beta:
            return True
        return False

    def _gendead(self):
        """Calculates probability of recovering or dying."""

        status = Status.INFECTED
        if random.randint(0, 100000) <= 100000 * self._mu:
            status = Status.RECOVERED
            if random.randint(0, 100000) <= 100000 * self._mu_d:
                status = Status.DEAD
        return status

    def step(self):
        """Calculate on iteration in simulation."""

        for idx_agent, contacts in enumerate(self._network):
            for idx_contact, contact in enumerate(contacts):
                if contact:
                    if self._agents[idx_agent].get_status() == Status.INFECTED \
                            and self._agents[idx_contact].get_status() == Status.SUSCEPTIBLE \
                            and self._make_contact():
                        self._agents[idx_contact].set_status(Status.INFECTED)

        for agent in self._agents:
            if agent.get_status() == Status.INFECTED:
                new_status = self._gendead()
                agent.set_status(new_status)

    def get_agents_stats(self):
        """Returns tuple with population of all states"""

        n_susceptible = 0
        n_infected = 0
        n_recovered = 0
        n_dead = 0

        for agent in self._agents:
            status = agent.get_status()

            if status == Status.SUSCEPTIBLE:
                n_susceptible += 1
            elif status == Status.INFECTED:
                n_infected += 1
            elif status == Status.RECOVERED:
                n_recovered += 1
            elif status == Status.DEAD:
                n_dead += 1
            
        stats =  (
            n_susceptible / self._n_agents,
            n_infected / self._n_agents,
            n_recovered / self._n_agents,
            n_dead / self._n_agents
        )

        return stats

    def get_agent_list(self):
        """Returns a list of the agents status"""
        status = [agent.get_status() for agent in self._agents]
        return status

    def get_adjacency_matrix(self):
        """Returns the adjacency_matrix of the network"""
        return self._network