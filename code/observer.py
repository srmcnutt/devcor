#!/usr/bin/env python

class Subject:
    def __init__(self, name):
      self.name = name
      self.subscribers = set()
    
    def register(self, name):
        self.subscribers.add(name)
    
    def unregister(self, name):
        self.subscribers.remove(name)
    
    def notify(self):
        for sub in self.subscribers:
            sub.update()
    
    def print_subscribers(self):
        for sub in self.subscribers:
            print(sub)

     

class Observer:
    def __init__(self, name):
      self.name = name
      self.counter = 1
    
    def update(self):
        self.counter += 5
    
    def __str__(self):
        return str(self.name)

def print_sub_counter(subject):
    print('subscriber update value:')
    for sub in subject.subscribers:
        print(f'{sub}: value: {sub.counter}')

if __name__ == "__main__":
    
    subject = Subject('subject')
    
    # make 10 observers and register with the subject
    for x in range(5):
        name = f'subscriber{x+1}'
        name = Observer(name)
        subject.register(name)
    
    # print out the subscriber list and current update value in the subscriber objects
    print(f'the following subscribers are registered:')
    print(subject.print_subscribers(), "\n")
    
    print('current subscriber update value')
    print_sub_counter(subject)    
    
    print('\n')
    # Call the update method on all the subscribers
    # This will cause them to increment their counters by 5
    
    print('updating the subscribers')
    subject.notify()
    
    # let's check the counter now to ensure the update method worked
    print_sub_counter(subject)

    


        




