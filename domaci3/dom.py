import numpy.random as rnd
import numpy as np

default_agent_graph = {
	0: [1],
	1: [0, 2, 3, 4],
	2: [0, 3],
	3: [1, 2],
	4: [1]
}

"""
	One thing that might be missing here is implementing this whole thing
	so that agents also communicate about the measurements rather than
	just averages

	Also implementing this to be more asynchronous but who was the time

	Another cheeky idea is to check has the mean of the agent values been
	going up or down and based on that say that the consensus is the min
	or max of does values
"""
def consensus(value, alpha, iter_count, var, eps, agent_graph=None):
	"""
		Function that does more or less everything
			* value - the actual value the agents are supposed to converge on
			* alpha - the weight of the new measurement
			* iter_count - self-explanatory
			* var - the percentage the value will vary - noise percentage
				+ if set to 0.3 the simulated values of measurements will be
				  in the range of 0.7 and 1.3 times of value
			* eps - convergence, if the mean of the agents doesn't change for
			  certain amount of iterations the algorithm will end
			* a graph of the agents, the key is and integer, and the value
			  is an array of agent indices in the graph
	"""
	if agent_graph is None:
		agent_graph = default_agent_graph
	
	agent_vals = ((rnd.rand(len(agent_graph)) - 0.5) * 2 * var + 1) * value

	for i in range(iter_count):
		for agent in agent_graph:
			u = 0
			for adj in agent_graph[agent]:
				u += (agent_vals[adj] - agent_vals[agent])
			u = u / len(agent_graph[agent])
			
			new_m = ((rnd.rand() - 0.5) * 2 * var + 1) * value
			b = (new_m - agent_vals[agent]) * alpha

			agent_vals[agent] += b + u

	return agent_vals


VALUE = 69

alpha = 0.01
ITERATIONS = 1000

vals = consensus(VALUE, alpha, ITERATIONS, 0.5, 1e-3, None)	
print(vals)
