import numpy as np
import requests
from scipy import stats

from settings import ATTEMPTS_NUMS, CUBE_FACES, TOTAL_DICES, URL


class ThompsonSampling:
    def __init__(self, total_dices: int = TOTAL_DICES, cube_faces: int = CUBE_FACES):
        self.total_dices = total_dices
        self.alphas = np.ones(shape=(total_dices, cube_faces))

    def generate_dice_num(self) -> int:
        expected_dices = []
        for dice_num in range(self.total_dices):
            dirichlet_rvs = self._get_dirichlet_rvs(dice_num)
            expected_dices.append(np.argmax(dirichlet_rvs))
        return np.random.choice([i for i in range(len(expected_dices)) if expected_dices[i] == max(expected_dices)]) + 1

    def update_alphas(self, dice_num: int):
        realization = requests.get(URL, params={'dice_num': dice_num}).json()['realization']
        self.alphas[dice_num - 1][realization - 1] += 1

    def _get_dirichlet_rvs(self, dice_num: int) -> int:
        return stats.dirichlet(alpha=self.alphas[dice_num]).rvs()[0]


def thompson_sampling_dice_num() -> int:
    thompson_sampling = ThompsonSampling()
    for _ in range(ATTEMPTS_NUMS):
        dice_num = thompson_sampling.generate_dice_num()
        thompson_sampling.update_alphas(dice_num)
    return thompson_sampling.generate_dice_num()
