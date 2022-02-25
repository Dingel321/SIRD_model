from simulation import Simulation


def main():
    n_agents = 144
    n_init_infected = 5
    n_steps = 100
    beta = 0.25
    mu = 0.1
    mu_d = 0.01

    sim = Simulation(n_steps, beta, mu, mu_d, n_agents, n_init_infected)
    sim.run()
    sim.show_results()


if __name__ == '__main__':
    main()
