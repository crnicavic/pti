from model import Model
from broker import Broker

broker = Broker(5, 10, 15)
model = Model(broker)

values = model.run()
model.visualize_results(values)
model.broker.visualize_graph()