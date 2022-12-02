import numpy as np

from utils import read_proba_distribution


class Dices:
    def __init__(self, file_name: str):
        self.proba_distributions = read_proba_distribution(file_name)

    def generate_sample(self, dice_num: int, sample_size: int = 1) -> int:
        probabilities = self.proba_distributions[str(dice_num)]
        return int(np.random.choice(a=len(probabilities), size=sample_size, p=probabilities)[0]) + 1
