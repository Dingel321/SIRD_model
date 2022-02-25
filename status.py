"""Module defining the agent status"""

from enum import Enum


class Status(Enum):
    """Class defining the agent status"""

    SUSCEPTIBLE = 'susceptible'
    INFECTED = 'infected'
    RECOVERED = 'recovered'
    DEAD = 'dead'
