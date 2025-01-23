from broker import Broker


class Model:
    def __init__(self, broker):
        self.broker = broker

    def run(self, max_iterations=1000, tolerance=1e-3):
        iteration = 0
        print(self.broker)
        while iteration < max_iterations:
            self.broker.update_agents()
            iteration += 1
            if iteration % 50 == 0:
                print(self.broker)

