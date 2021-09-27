class Observable:
    def __init__(self):
        self.observers = set() 
    def register(self, who):
        self.observers.add(who)
    def unregister(self, who):
        self.observers.discard(who) 
    def dispatch(self, message):
        for observer in self.observers:
            observer.update(message) 

class Observer:
    def __init__(self, name):
        self.name = name 
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))