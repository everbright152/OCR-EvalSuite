from src.metrics.cer import cer
from src.metrics.wer import wer


def evaluate(predicted, ground_truth, inference_time):
    return {
        "cer": cer(predicted, ground_truth),
        "wer": wer(predicted, ground_truth),
        "time": inference_time
    }
    