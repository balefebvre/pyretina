import numpy as np


def extract_rising_fronts(y, threshold=+500.0):
    """Extract rising front of each trigger.

    Parameters
    ----------
    y: numpy.ndarray
    threshold: float, optional
        The default values is +500.0

    """
    # TODO complete docstring.

    rising_fronts = []

    for k in range(1, len(y) - 1):
        if y[k-1] > y[k] and y[k] <= y[k+1]:
            l = k + 1
            while l+1 < len(y) and y[l] <= y[l+1]:
                l += 1
            a = y[l] - y[k]
            if a > threshold:
                m = k
                while m <= l and y[m+1] - y[m] < +50.0:
                    m += 1
                rising_fronts.append(m)

    rising_fronts = np.array(rising_fronts)

    return rising_fronts


def extract_falling_fronts(y, threshold=+500.0):
    """Extract falling front of each trigger.

    Parameters
    ----------
    y: numpy.ndarray
    threshold: float, optional
        The default value is +500.0.

    """
    # TODO complete docstring.

    falling_fronts = []

    for k in range(1, len(y) - 1):
        if y[k-1] >= y[k] and y[k] < y[k+1]:
            l = k - 1
            while l-1 > 0 and y[l-1] >= y[l]:
                l -= 1
            a = y[l] - y[k]
            if a > threshold:
                m = k
                while l <= m and y[m-1] - y[m] < +50.0:
                    m -= 1
                falling_fronts.append(m)

    falling_fronts = np.array(falling_fronts)

    return falling_fronts
