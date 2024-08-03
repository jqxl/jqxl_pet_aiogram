from enum import Enum


class Commands(str, Enum):
    START = 'start'


class Callbacks(str, Enum):
    YES = 'YES'
    NO = 'NO'
    WEBAPP = 'WEBAPP'