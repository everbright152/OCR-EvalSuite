import Levenshtein


def cer(predicted: str, ground_truth: str) -> float:
    if not ground_truth:
        return 0.0

    distance = Levenshtein.distance(predicted, ground_truth)
    return distance / len(ground_truth)
    