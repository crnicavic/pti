from broker import Broker
import matplotlib.pyplot as plt

class Model:
    def __init__(self, broker):
        self.broker = broker

    def run(self, max_iterations=1000, tolerance=1e-3):
        iteration = 0
        values = []
        print(self.broker)
        while iteration < max_iterations:
            values.append(self.broker.update_agents())
            iteration += 1
            if iteration % 50 == 0:
                print(self.broker)
        return values

    def visualize_results(self, values):
        plt.plot(values)
        plt.xlabel('Iterations')
        plt.ylabel('Temperature Values')
        l = ''
        for i in range(self.broker.num_agents):
            l += f'{i}'
        plt.legend(l,loc='upper right')
        plt.show()
