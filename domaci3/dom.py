import numpy.random as rnd

default_agent_graph = {
	0: [1],
	1: [0, 2, 3, 4],
	2: [0, 3],
	3: [1, 2],
	4: [1]
}

def consensus(value, alpha, iter_count, var, eps, agent_graph):
	if agent_graph is None:
		agent_graph = default_agent_graph
	
	agent_vals = (rnd.rand(len(agent_graph)) + var) * value

	for i in range(iter_count):
		for agent in agent_graph:
			gamma = 1 / len(agent_graph[agent])
			u = 0
			for adj in agent_graph[agent]:
				u += gamma * (agent_vals[adj] - agent_vals[agent])
			
			# new measurement
			new_m = rnd.uniform(VALUE*0.5, 1.5*VALUE)
			b = (new_m - agent_vals[agent]) * alpha

			agent_vals[agent] += b + u

	return agent_vals


VALUE = 69

alpha = 0.01
ITERATIONS = 1000

vals = consensus(VALUE, alpha, ITERATIONS, 0.5, 1e-3, None)	
print(vals)
