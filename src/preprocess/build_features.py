import pandas as pd;

def merge_dataset(data1, data2, on):
    """

    :param data1: first dataset to be merged
    :param data2: second dataset to be merged
    :param on: common id/feature on which we join the data sets
    :return: resultant merged data frame
    """
    return pd.merge(data1, data2, how='left', on=on)

