import gevent

class Subscriber:
    def __init__(self, observer):
        self.observer = observer
        self.queue = gevent.queue.Queue()
        self.active = True

    def send(self, msg):
        #logger.debug(f"msg: {msg}")
        #self.queue.put(msg)
        self.observer.on_next(msg)

    def receive(self):
        self.queue.get()

class Hub:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def send(self, msg):
        gevent.spawn(self.publish(msg))

    def publish(self, msg):
        for subscriber in self.subscribers:
            subscriber.send(msg)
