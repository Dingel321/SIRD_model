from environment import Environment

def main():
    environment = Environment(0.2, 0.1, 0.001, 9)
    
    for i in range(20):
        environment.step()
        print(environment.get_agents_status())

if __name__ == '__main__':
    main()