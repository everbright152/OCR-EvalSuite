import Levenshtein


def wer(predicted: str, ground_truth: str) -> float:
    pred_words = predicted.split()
    gt_words = ground_truth.split()

    if not gt_words:
        return 0.0

    distance = Levenshtein.distance(" ".join(pred_words),
                                    " ".join(gt_words))

    return distance / len(gt_words)
    