import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx

from SIRD.environment import Environment
from SIRD.status import Status


class Simulation:
    """Class for simulating SIRD Model"""

    def __init__(self, n_steps, beta, mu, mu_d, n_agents, n_init_infected=1, video=False, contact_network='grid'):
        self._environment = Environment(beta, mu, mu_d, n_agents, n_init_infected, contact_network)
        self._steps = n_steps
        self._results = {Status.SUSCEPTIBLE: [], Status.INFECTED: [], Status.RECOVERED: [], Status.DEAD: []}
        self._video = video
        self._contact_network = contact_network
        if self._video:
            adj_matrix = self._environment.get_adjacency_matrix()
            self._network = nx.convert_matrix.from_numpy_matrix(adj_matrix)
            self._agents_status = []

    def _evaluate(self):
        self._environment.step()
        n_sus, n_inf, n_reco, n_dead = self._environment.get_agents_stats()
        self._results[Status.SUSCEPTIBLE].append(n_sus)
        self._results[Status.INFECTED].append(n_inf)
        self._results[Status.RECOVERED].append(n_reco)
        self._results[Status.DEAD].append(n_dead)
        if self._video:
            self._agents_status.append(self._environment.get_agent_list())

    def run(self):
        """Runs the SIRD simulation"""
        for _ in range(self._steps):
            self._evaluate()

    def show_results(self, show=True):
        """Shows the population evolution over time"""
        fig, ax = plt.subplots()
        ax.plot(self._results[Status.SUSCEPTIBLE], label='S')
        ax.plot(self._results[Status.INFECTED], label='I')
        ax.plot(self._results[Status.RECOVERED], label='R')
        ax.plot(self._results[Status.DEAD], label='D')
        ax.xlabel('Iterations')
        ax.ylabel('Percentage')
        ax.legend()
        if show:
            plt.show()
        else:
            return fig

    def generate_video(self, show=True):
        """Generates a video of the simulation results"""
        if not self._video:
            raise Exception('Video generation was set to False. Set video=True')

        
        def translate_color(status):
            if status == Status.SUSCEPTIBLE:
                return 'blue'
            elif status == Status.INFECTED:
                return 'red'
            elif status == Status.RECOVERED:
                return 'green'
            elif status == Status.DEAD:
                return 'black'

        def animate(frame):
            ax.cla()
            node_color = [translate_color(agent_status) for agent_status in agents_status[frame]]
            nx.draw(network, node_color=node_color, pos=pos)
            return fig

        network = self._network
        agents_status = self._agents_status
        pos = nx.spring_layout(network)

        fig, ax = plt.subplots()
        plot_anim = animation.FuncAnimation(
            fig,
            animate,
            frames=range(self._steps),
            interval=200
        )
        if show:
            plt.axis('off')
            plt.show()
        return plot_anim
