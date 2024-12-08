import numpy.random as rnd
import numpy as np

default_agent_graph = {
	0: [1],
	1: [0, 2, 3, 4],
	2: [0, 3],
	3: [1, 2],
	4: [1]
}

def calculate_weights(agent_graph):
	"""
		It was an idea but not a very good one
		weights are based on how many neighbours each node has
	"""
	# it is wasteful but simple and a bit faster than tuples
	weights_dict = dict()
	for agent in agent_graph:
		weights_dict[agent] = np.zeros(len(agent_graph))
		total_adj = 0
		for adj in agent_graph[agent]:
			total_adj += len(agent_graph[adj])
		weights_dict[agent][adj] = len(agent_graph[adj]) / total_adj
	return weights_dict

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
	
	agent_vals = (rnd.rand(len(agent_graph)) + var) * value


	for i in range(iter_count):
		for agent in agent_graph:
			total_adj = 0
				
			u = 0
			gamma = 1 / len(agent_graph[agent])
			for adj in agent_graph[agent]:
				u += gamma * (agent_vals[adj] - agent_vals[agent])
			
			new_m = (rnd.rand() + var) * value
			b = (new_m - agent_vals[agent]) * alpha

			agent_vals[agent] += b + u

	return agent_vals


VALUE = 69

alpha = 0.01
ITERATIONS = 1000

vals = consensus(VALUE, alpha, ITERATIONS, 0.5, 1e-3, None)	
print(vals)
