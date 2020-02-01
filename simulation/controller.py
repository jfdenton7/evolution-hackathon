from simulation.config import CARC_WATER, CARC_FERR, CARC_AA
import os
import re
import json
from os import path
from copy import deepcopy
import datetime


class Controller:

    def __init__(self, mutigen):
        if mutigen is CARC_WATER:
            self.mutigen = 'WATER'
        elif mutigen is CARC_FERR:
            self.mutigen = 'FERR'
        elif mutigen is CARC_AA:
            self.mutigen = 'AA'
        else:
            self.mutigen = ''

        self.time = datetime.datetime.now().strftime("%H:%M:%S")
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
        'name': st
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
        print(self.trials)
        trials = list(map(
            self.__format_trials,
            self.trials
        ))

        # print(trials)

        self.json = {
            'name': f'evo_{self.mutigen}_{self.time}',
            'trials': trials
        }

    def __send_json(self):
        if path.exists(f'data{self.mutigen}.json'):
            os.remove(f'data{self.mutigen}.json')

        with open(f'data{self.mutigen}.json', 'w+', encoding='utf-8') as f:
            print(f)
            json.dump(self.json, f, ensure_ascii=False, indent=4)

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
            'x': x,
            'y': y,
            'pop': colony.num_cells(),
            'radius': colony.get_radius()
        }









