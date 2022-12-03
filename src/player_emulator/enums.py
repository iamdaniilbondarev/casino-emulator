from enum import Enum


class Strategies(Enum):
    epsilon_greedy = 'epsilon_greedy'
    thompson_sampling = 'thompson_sampling'
    all = 'all'


class StepType(Enum):
    explore = 'explore'
    exploit = 'exploit'
