import random

agent_graph = {
	0: [1],
	1: [0, 2, 3, 4],
	2: [0, 3],
	3: [1, 2],
	4: [1]}

VALUE = 69

gamma = 0.01

ITERATIONS = 1000
agent_vals = [random.uniform(VALUE*0.8, 1.2*VALUE) for _ in range(len(agent_graph))]

for _ in range(ITERATIONS):
	for agent in agent_graph:
		for adj in agent_graph[agent]:
			agent_vals[agent] += gamma * (agent_vals[adj] - agent_vals[agent])

print(agent_vals)
	
