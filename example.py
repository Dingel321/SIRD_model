import matplotlib.pyplot as plt
import networkx as nx
from SIRD.simulation import Simulation


def main():
    n_agents = 300
    n_init_infected = 5
    n_steps = 100
    beta = 0.45
    mu = 0.1
    mu_d = 0.01

    contact_network = nx.watts_strogatz_graph(n_agents, k=4, p=0.03)
    #contact_network = nx.erdos_renyi_graph(n_agents, p=0.002)
    #contact_network = nx.barabasi_albert_graph(n_agents, m=1)

    sim = Simulation(
        n_steps, 
        beta, 
        mu, 
        mu_d, 
        n_agents, 
        n_init_infected,  
        video=True, 
        contact_network=contact_network
    )

    sim.run()
    print(len(sim._agents_status))
    sim.generate_video()
    #sim.show_results()
    

if __name__ == '__main__':
    main()
