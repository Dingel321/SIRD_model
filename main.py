import matplotlib.pyplot as plt
from environment import Environment


def main():
    n_agents = 288
    n_init_infected = 3
    n_steps = 100
    beta = 0.25
    mu = 0.1
    mu_d = 0.01

    susceptible = []
    infected = []
    recovered = []
    dead = []

    environment = Environment(beta, mu, mu_d, n_agents, n_init_infected)
    
    for i in range(n_steps):
        n_sus, n_inf, n_reco, n_dead = environment.get_agents_status()
        susceptible.append(n_sus)
        infected.append(n_inf)
        recovered.append(n_reco)
        dead.append(n_dead)

        environment.step()

    plt.plot(susceptible, label='susceptible')
    plt.plot(infected, label='infected')
    plt.plot(recovered, label='recovered')
    plt.plot(dead, label='dead')
    plt.legend()
    plt.xlabel('steps')
    plt.ylabel('percentage')
    plt.title(f'agents = {n_agents}')
    plt.ylim((0, 1))
    plt.xlim((0, n_steps))
    plt.show()


if __name__ == '__main__':
    main()
