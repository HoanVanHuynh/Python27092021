from observer1 import Subscriber, Publisher 

pub = Publisher() 

bob = Subscriber('Bob') 
alice = Subscriber('Alice') 
john = Subscriber('John') 


# these subscribers have to register with the publisher 
pub.register(bob)
pub.register(alice) 
pub.register(john) 

pub.dispatch("It's lunchtime") 
pub.unregister(john)
pub.dispatch("Time for dinner")