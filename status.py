from enum import Enum


class Status(Enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERD = 2

'''
Example : 
agent = Agent(Status.SUSCEPTIBLE)

https://docs.python.org/3/library/enum.html
'''