class Agent():

    def __init__(self, status, infected_days) -> None:
        self._status = status
        self._days_of_sick = 0
        self._infected_days = infected_days
          
    def get_status(self) -> str:
        """Return current status of the agent"""

        return self._status

    def set_status(self, new_status) -> None:
        """Set The new current state of the agent"""

        if self._status == 'susceptible' and new_status == 'recovered':
            raise Exception('Wrong agent status!')
        self._status = new_status

    def add_sick_day(self) -> None:
        """Increment days of sickness"""

        if self._status == 'infected':
            self._days_of_sick += 1
        if self._days_of_sick > self._infected_days:
            self._reset_sick_days()
            
    def _reset_sick_days(self) -> None:
        self._days_of_sick = 0
        

