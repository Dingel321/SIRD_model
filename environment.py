import networkx as nx
import numpy as np
import random
from agent import Agent


class Environment:
    """Environment class representing a single simulation setting."""

    def __init__(self, beta, mu, mu_d, N):
        self._beta = beta
        self._mu = mu
        self._mu_d = mu_d
        self._N = N
        self._network = self._generate_network()
        self._agents = self._generate_agents()

    def _generate_network(self):
        """Returns adjacency matrix of network."""

        network_dic = nx.grid_2d_graph(
            int(np.sqrt(self._N)),
            int(np.sqrt(self._N)),
            False
        )  # TODO ungerades N
        return nx.convert_matrix.to_numpy_array(network_dic, dtype=int)

    def _generate_agents(self, init_infected=1):
        """Returns list of agents."""

        agents = []
        for i in range(self._N):
            if i < init_infected:
                agents.append(Agent('infected'))
            else:
                agents.append(Agent('susceptible'))
        return agents

    def _make_contact(self):
        """Determines if contact is infectious"""

        if random.randint(0, 100000) <= 100000 * self._beta:
            return True
        return False

    def _gendead(self):
        """Calculates probability of recovering or dying."""

        status = 'infected'
        if random.randint(0, 100000) <= 100000 * self._mu:
            status = 'recovered'
            if random.randint(0, 100000) <= 100000 * self._mu_d:
                status = 'dead'
        return status

    def step(self):
        """Calculate on iteration in simulation."""
        for idx_agent, contacts in enumerate(self._network):
            for idx_contact, contact in enumerate(contacts):
                if contact:
                    if self._agents[idx_agent].get_status() == 'infected' \
                            and self._agents[idx_contact].get_status() == 'susceptible' \
                            and self._make_contact():
                        self._agents[idx_contact].set_status('infected')

        for agent in self._agents:
            if agent.get_status() == 'infected':
                new_status = self._gendead()
                agent.set_status(new_status)

    def get_agents_status(self):
        n_susceptible = 0
        n_infected = 0
        n_recovered = 0
        n_dead = 0

        for agent in self._agents:
            status = agent.get_status()

            if status == 'susceptible':
                n_susceptible += 1
            elif status == 'infected':
                n_infected += 1
            elif status == 'recovered':
                n_recovered += 1
            elif status == 'dead':
                n_dead += 1
            
        stats =  (
            n_susceptible / self._N,
            n_infected / self._N,
            n_recovered / self._N,
            n_dead / self._N
        )

        return stats
