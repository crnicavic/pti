import numpy as np
import networkx as nx
from agent import Agent
import matplotlib.pyplot as plt
import random

class Broker:
    def __init__(self, num_agents, starting_value, noise=5):

        self.num_agents = num_agents
        self.agents = [Agent(i, starting_value, noise ) for i in range(num_agents)]
        self.graph = self.create_directed_graph()
        self.graph_matrix = nx.to_numpy_array(self.graph)

    def create_directed_graph(self, p=0.4):
        G = nx.DiGraph()
        p = np.log(self.num_agents) / self.num_agents
        G.add_nodes_from(range(self.num_agents))
        for i in range(self.num_agents):
            for j in range(self.num_agents):
                if i != j and random.random() < p:
                    G.add_edge(i, j, weight=1)
        return G

    def visualize_graph(self):
        # Set up the position layout for the graph
        pos = nx.spring_layout(self.graph)  # You can use different layouts like `circular_layout`, `shell_layout`, etc.
        
        # Draw the graph with labels
        plt.figure(figsize=(self.num_agents, self.num_agents))
        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color='lightblue', arrows=True, font_size=12)
        
        # Display the plot
        plt.title("Directed Graph")
        plt.show()

    def get_neighbor_values(self, agent_id):
        neighbors = list(self.graph.neighbors(agent_id))
        return [self.agents[neighbor].value for neighbor in neighbors], neighbors

    def update_agents(self):
        new_values = []
        for agent in self.agents:
            neighbor_states, neighbors = self.get_neighbor_values(agent.id)
            weights = [self.graph[agent.id][neighbor]['weight'] for neighbor in neighbors]
            agent.update_value(weights, neighbor_states)
            new_values.append(agent.value)
        return new_values

    def check_convergence(self, tolerance=1e-3):
        pass

    def __repr__(self):
        return f"Broker(num_agents={self.num_agents}, \nagents=\n{self.agents})\n"