import json
from pathlib import Path


dice_emulator_dir = Path(__file__).parent


def read_proba_distribution(file_name: str) -> dict[str, list[float]]:
    with open(dice_emulator_dir / file_name) as f:
        probabilities = json.load(f)
    return probabilities
