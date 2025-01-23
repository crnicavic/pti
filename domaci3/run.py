from model import Model
from broker import Broker

broker = Broker(10, 10, 15)
model = Model(broker)

values = model.run()

model.broker.visualize_graph()
model.visualize_results(values)