from protocol import Model
from broker import Broker

broker = Broker(5, 10, 15)
model = Model(broker)

model.run()
model.broker.visualize_graph()