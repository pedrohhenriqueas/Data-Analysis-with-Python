import numpy as np
def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    numbers_3x3 = np.array(numbers).reshape(3, 3)

    result = {
        'mean': [
            np.mean(numbers_3x3, axis=0).tolist(),
            np.mean(numbers_3x3, axis=1).tolist(),
            np.mean(numbers_3x3)
        ],
        'variance': [
            np.var(numbers_3x3, axis=0).tolist(),
            np.var(numbers_3x3, axis=1).tolist(),
            np.var(numbers_3x3)
        ],
        'standard deviation': [
            np.std(numbers_3x3, axis=0).tolist(),
            np.std(numbers_3x3, axis=1).tolist(),
            np.std(numbers_3x3)
        ],
        'max': [
            np.max(numbers_3x3, axis=0).tolist(),
            np.max(numbers_3x3, axis=1).tolist(),
            np.max(numbers_3x3)
        ],
        'min': [
            np.min(numbers_3x3, axis=0).tolist(),
            np.min(numbers_3x3, axis=1).tolist(),
            np.min(numbers_3x3)
        ],
        'sum': [
            np.sum(numbers_3x3, axis=0).tolist(),
            np.sum(numbers_3x3, axis=1).tolist(),
            np.sum(numbers_3x3)
        ]
    }

    return result
