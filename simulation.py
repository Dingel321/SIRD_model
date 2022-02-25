import matplotlib.pyplot as plt

from environment import Environment
from status import Status


class Simulation:
    """Class for simulating SIR Model"""

    def __init__(self, N, beta, mu, mu_d, n_agents, n_init_infected=1, contac_network='grid',video=False):
        self._environment = Environment(beta, mu, mu_d, n_agents, n_init_infected)
        self._N = N
        self._results = {Status.SUSCEPTIBLE: [], Status.INFECTED: [], Status.RECOVERED: [], Status.DEAD: []}
        if video:
            pass

    def _evaluate(self):
        self._environment.step()
        n_sus, n_inf, n_reco, n_dead = self._environment.get_agents_status()
        self._results[Status.SUSCEPTIBLE].append(n_sus)
        self._results[Status.INFECTED].append(n_inf)
        self._results[Status.RECOVERED].append(n_reco)
        self._results[Status.DEAD].append(n_dead)

    def run(self):
        """Runs the SIRD simulation"""
        for _ in range(self._N):
            self._evaluate()

    def show_results(self):
        """Shows the population evolution over time"""
        plt.plot(self._results[Status.SUSCEPTIBLE], label='S')
        plt.plot(self._results[Status.INFECTED], label='I')
        plt.plot(self._results[Status.RECOVERED], label='R')
        plt.plot(self._results[Status.DEAD], label='D')
        plt.xlabel('Iterations')
        plt.ylabel('Percentage')
        plt.legend()

    def generate_video(self):
        pass