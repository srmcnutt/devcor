#!/usr/bin/env python

import datetime
import requests 

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
        raise NotImplementedError("children must implement")
    
    def __str__(self):
        return str(self.name)

class RedObserver(Observer):
    def update(self):
       self.counter = datetime.datetime.now()

class BlueObserver(Observer):
    def update(self):
        self.weather = requests.get('http://wttr.in/New+York?0')
        self.counter = self.weather.text
        
def print_sub_counter(subject):
    print('subscriber update value:')
    for sub in subject.subscribers:
        print(f'{sub}: value: {sub.counter}')


if __name__ == "__main__":
    
    subject = Subject('subject')
    
    # make 5 red observers and register with the subject
    for x in range(5):
        name = f'Red subscriber{x+1}'
        name = RedObserver(name)
        subject.register(name)

    # make 5 blue observers and register with the subject
    for x in range(5):
        name = f'Blue subscriber{x+1}'
        name = BlueObserver(name)
        subject.register(name)
    
    # print out the subscriber list and current update value in the subscriber objects
    print(f'the following subscribers are registered:')
    print(subject.print_subscribers(), '\n')
    
    print('current subscriber update value')
    print_sub_counter(subject)    
    print('\n')


    # Call the update method on all the subscribers
    # This will cause them to increment their counters by 5
    print('!----------------updating the subscribers------------------!\n')
    subject.notify()
    
    # let's check the counter now to ensure the update method worked
    print_sub_counter(subject)

    


        




