"""Module containing the agent class"""

from status import Status


class Agent():
    """Agent class for SIR model"""

    def __init__(self, status):
        self._status = status

    def get_status(self):
        """Return current status of the agent"""

        return self._status

    def set_status(self, new_status):
        """Set The new current state of the agent"""

        if self._status == Status.SUSCEPTIBLE and new_status == Status.RECOVERED:
            raise Exception('Wrong agent status!')
        self._status = new_status

