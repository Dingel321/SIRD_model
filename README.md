# SIRD_model
Python implementation of agent-based SIRD model  

To initalize the simulation just use the Simulation cunstructor.  
```
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
```  
To run the simulation just call the run() method.  

```
sim.run()
```  
To show the resulting population dynamics, just call the show_results() method.  

```
sim.show_results()
```