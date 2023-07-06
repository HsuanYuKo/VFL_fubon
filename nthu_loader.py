import pandas as pd
import random
from utils import move_item_to_start_, move_item_to_end_

item = ['x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14','x15','x16','x17','x18','x19','x20','x21','x22','x23','x24','x25','x26']

def load_nthu(nthu_path):
    print("Loading nthu from {}".format(nthu_path))
    nthu_data = pd.read_csv(nthu_path)

    nthu_data.drop(item)

    nthu_data.info(verbose=True)

    labels = nthu_data['x2'].to_numpy()
    nthu_data = nthu_data.drop(columns=['x2']).to_numpy()

    return nthu_data, labels


def load_both(party_path_A, party_path_B, active_party='nthu'):
    print("Loading A from {}".format(party_path_A))
    A_data = pd.read_csv(party_path_A)
    print("Loading B from {}".format(party_path_B))
    B_data = pd.read_csv(party_path_B)

    if active_party == 'nthu':
        labels = A_data['x2'].to_numpy()
        A_data.drop(columns=['x2'], inplace=True)

        # move lon and lat to end
        A_cols = list(A_data.columns)
        move_item_to_end_(A_cols, item)
        A_data = A_data[A_cols]
        print("Current A columns {}".format(A_data.columns))

        # B_data.drop(columns=['school_name'], inplace=True)

        # move lon and lat to start
        B_cols = list(B_data.columns)
        move_item_to_start_(B_cols, item)
        B_data = B_data[B_cols]
        print("Current B columns {}".format(B_data.columns))

        data1 = A_data.to_numpy()
        data2 = B_data.to_numpy()
    else:
        raise NotImplementedError

    return [data1, data2], labels



