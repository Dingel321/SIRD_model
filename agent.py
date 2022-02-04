class Agent():

    def __init__(self, status, infected_days) -> None:
        self._status = status
        self._days_of_sick = 0
        self._infected_days = infected_days
          
    def get_status(self) -> str:
        '''Returns current status of the agent'''

        return self._status

    def set_status(self, new_status) -> None:
        '''Set The new current state of the agent'''

        if self._status == 'suseptible' and new_status == 'recoverd':
            raise Exception('Wrong agent status!')
        self._status = new_status

    def add_sick_day(self) -> None:
        '''Increment days '''
        if self._status == 'suseptible':
            self._days_of_sick += 1
        if self._days_of_sick > self._infected_days:
            self._reset_sick_days()
            
    def _reset_sick_days(self) -> None:
        self._days_of_sick = 0
        

