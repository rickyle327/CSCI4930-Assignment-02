def Q_01(self):
    # Task 1: Compute mean, stdev, min, max, 25% percentile, median and 75% percentile of BWEIGHT target variable
    # in the full_dataset, and return the computed values as a numpy array containing these 7 numbers (respectively).

    # YOUR CODE HERE

    import numpy as np

    bweight = self.full_dataset.BWEIGHT.array

    mean = np.mean(bweight)
    stdev = np.std(bweight)
    b_min = min(bweight)
    b_max = max(bweight)
    l_perc = np.percentile(bweight, 25)
    med = np.median(bweight)
    u_perc = np.percentile(bweight, 75)

    return [mean, stdev, b_min, b_max, l_perc, med, u_perc]
