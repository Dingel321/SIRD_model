from agent import Agent
import networkx as nx
import numpy as np


class Environment:

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
        return nx.adjacency_matrix(network_dic).todense()

    def _generate_agents(self, init_infected=1, infected_days=5):
        """Returns list of agents."""

        agents = []
        for i in range(self._N):
            if i <= init_infected:
                agents.append(Agent('infected', infected_days))
            else:
                agents.append(Agent('susceptible', infected_days))
        return agents

    def _make_contact(self):
        """Calculates probability of infections contac."""

        pass

    def _gendead(self):
        """Calculates probability of recovering or dying."""

        pass

    def step(self):
        """Calculte on iteration in simulation."""
        
        for idx_agent, contacts in enumerate(self._network):
            for idx_contact, contact in enumerate(contacts, start=idx_agent):
                if contact:
                    pass
                    #ist da ein Kontakt?
                    #ist idx_agent krank?
                    #wird idx_contact krank?
                        #if idx_contact krank:set new status von idx_contact, wenn krank
            self._agents[idx_agent].add_sick_days()


    def get_agents_status(self):
        pass # Idee : return tupel with (S/N, I/N, R/N)

