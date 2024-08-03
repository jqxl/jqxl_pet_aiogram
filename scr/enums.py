from enum import Enum


class Commands(str, Enum):
    start = 'start'


class Callbacks(str, Enum):
    yes = 'YES'
    no = 'NO'