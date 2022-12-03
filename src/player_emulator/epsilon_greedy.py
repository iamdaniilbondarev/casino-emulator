import numpy as np
import requests

from enums import StepType
from settings import ATTEMPTS_NUMS, EPSILON, TOTAL_DICES, URL


class EpsilonGreedy:
    def __init__(self, epsilon: float = EPSILON, total_dices: int = TOTAL_DICES):
        self.epsilon = epsilon
        self.total_dices = total_dices
        self.means_distribution = [0 for _ in range(total_dices)]
        self.realizations = {i: [] for i in range(1, total_dices + 1)}

    def explore_step(self):
        explore_indexes = [
            index + 1 for index, val in enumerate(self.means_distribution) if val != max(self.means_distribution)
        ]
        if explore_indexes:
            dice_num = np.random.choice(explore_indexes)
        else:
            dice_num = np.random.randint(low=1, high=self.total_dices + 1)
        self.update_realizations(dice_num)

    def exploit_step(self):
        exploit_indexes = [
            index + 1 for index, val in enumerate(self.means_distribution) if val == max(self.means_distribution)
        ]
        dice_num = np.random.choice(exploit_indexes)
        self.update_realizations(dice_num)

    def update_realizations(self, dice_num: int):
        realization = requests.get(URL, params={'dice_num': dice_num}).json()['realization']
        self.realizations[dice_num].append(realization)

    def update_means_distribution(self):
        self.means_distribution = []
        for realization in self.realizations.values():
            if realization:
                self.means_distribution.append(sum(realization) / len(realization))
            else:
                self.means_distribution.append(0.0)

    def choose_step(self) -> StepType:
        return StepType.explore if np.random.random() < self.epsilon else StepType.exploit

    def get_optimal_dice(self) -> int:
        return np.argmax(self.means_distribution) + 1


def epsilon_greedy_dice_num() -> int:
    epsilon_greedy = EpsilonGreedy()
    for _ in range(ATTEMPTS_NUMS):
        step_type = epsilon_greedy.choose_step()
        match step_type:
            case StepType.explore:
                epsilon_greedy.explore_step()
            case StepType.exploit:
                epsilon_greedy.exploit_step()
        epsilon_greedy.update_means_distribution()
    return epsilon_greedy.get_optimal_dice()
