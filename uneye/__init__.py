from .classifier import DNN


def weights_dir():
    from pathlib import Path

    return Path(__file__).parent / "weights"
