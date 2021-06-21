# https://dev.to/mandrewcito/lazy-pub-sub-python-implementation-3fi8

class EventChannel:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        if event not in self.subscribers.keys():
            self.subscribers[event] = [callback]
        else:
            (self.subscribers[event]).append(callback)

    def unsubscribe(self, event, callback):
        if event not in self.subscribers.keys():
            raise Exception("Not a valid Event")
        else:
            events = (self.subscribers[event])
            idx = events.index(callback)
            del events[idx]

    def publish(self, event, args):
        if event not in self.subscribers.keys():
            raise Exception("Not a valid Event")
        else:
            for callback in self.subscribers[event]:
                print(callback(args))

ech = EventChannel()
ech.subscribe("hi", lambda x: x.lower())
ech.subscribe("hi", lambda x: x.upper())

ech.publish("hi", "Hello world")
