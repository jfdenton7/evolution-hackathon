from copy import deepcopy
from datetime import datetime


class Controller:

    def __init__(self, mutigen, time):
        self.mutigen = mutigen
        self.time = datetime().now().strftime('%H:%M:%S')
        self.trials = []

    def send_data(self, colonies, max_col, max_col_sz, radius, final):
        self.trials.append((deepcopy(colonies), deepcopy(max_col), max_col_sz, radius, len(self.trials) + 1))
        if final:
            self.__pack_json()
            self.__send_json()
            self.__reset()

    def __pack_json(self):
        """
        Pack a json with trial data according to the following format::

        {
        'name': str
        'trials': [

        {
        'trial_id': int
        'colonies': [
        { 'colony_id': int
        'x': int
        'y': int
        'pop': pop
        'radius': radius
        },
        ...]
        },
        ...
        ]
        }
        :return:
        """

        trials = list(map(
            self.__format_trials,
            self.trials
        ))

        js = {
            'name': f'evo_{self.mutigen}_{self.time}',
            'trials': trials
        }

        pass

    def __send_json(self):
        pass

    def __reset(self):
        self.mutigen = None
        self.time = None
        self.trials = []

    def __format_trials(self, info):
        colonies, max_col, max_sz, rad, trial_id = info

        col_info = list(map(
            self.__format_colonies,
            colonies
        ))

        return {
            'trial_id': trial_id,
            'max_col_id': max_col.id,
            'max_sz': max_sz,
            'max_rad': rad,
            'colonies': col_info
        }

    def __format_colonies(self, colony):
        y, x = colony.pos
        return {
            'colony_id': colony.id,
            'x':
        }









