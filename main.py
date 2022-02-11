import matplotlib.pyplot as plt
from environment import Environment


def main():
    suseptible = []
    infected = []
    recovered = []
    dead = []

    environment = Environment(0.2, 0.1, 0.3, 11)
    
    for i in range(100):
        n_sus, n_inf, n_reco, n_dead = environment.get_agents_status()
        suseptible.append(n_sus)
        infected.append(n_inf)
        recovered.append(n_reco)
        dead.append(n_dead)

        environment.step()

    plt.plot(suseptible)
    plt.plot(infected)
    plt.plot(recovered)
    plt.plot(dead)

if __name__ == '__main__':
    main()
    plt.plot([1, 2, 3])