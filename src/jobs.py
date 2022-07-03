from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    # list_to_return = []

    with open(path, 'r') as file:
        jobs = csv.DictReader(file)
        # for index in jobs:
        # list_to_return.append(index)

        return [index for index in jobs]
