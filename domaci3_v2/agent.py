import numpy as np


class Agent:
    def __init__(self, id, starting_value = 20, noise=5):
        self.id = id
        self.noise = np.random.uniform(0, noise)
        self.value = starting_value + self.noise
        self.neighbours = []

    def get_value(self):
        return self.value

    def get_id(self):
        return self.id

    def get_neighbours(self):
        return self.neighbours

    def update_value(self, weights, neighbour_values, alpha = 0.01):
        average = np.mean(weights[i] * (neighbour_values[i] - self.value) for i in range(len(neighbour_values)))
        self.value += alpha * (average - self.value)

    def __repr__(self):
        return f"Agent(id={self.id}, state={self.value:.2f})"