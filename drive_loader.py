import pandas as pd
import random
from utils import move_item_to_start_, move_item_to_end_

item = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37']
#item = ['0','1','2','3','4']
# index = [0, 1, 2, 3, 4]

def load_drive(drive_path):
    print("Loading drive from {}".format(drive_path))
    drive_data = pd.read_csv(drive_path)

    drive_data.drop(columns=['22', '23', '24', '25', '26'])

    drive_data.info(verbose=True)

    labels = drive_data['label'].to_numpy()
    drive_data = drive_data.drop(columns=['label']).to_numpy()

    return drive_data, labels


def load_both(drive_path_A, drive_path_B, active_party='drive'):
    print("Loading A from {}".format(drive_path_A))
    A_data = pd.read_csv(drive_path_A)
    print("Loading B from {}".format(drive_path_B))
    B_data = pd.read_csv(drive_path_B)
    # tar_index = random.sample(index, 1)


    if active_party == 'drive':
        labels = A_data['label'].to_numpy()
        A_data.drop(columns=['label'], inplace=True)

        # move lon and lat to end
        A_drive_cols = list(A_data.columns)
        move_item_to_end_(A_drive_cols, item)
        # move_item_to_end_(A_drive_cols, [item[tar_index[0]]])
        A_data = A_data[A_drive_cols]
        print("Current A columns {}".format(A_data.columns))

        # B_data.drop(columns=['school_name'], inplace=True)

        # move lon and lat to start
        B_drive_cols = list(B_data.columns)
        # delete_index = [x for x in index if x not in tar_index]
        # B_drive_cols.remove(item[delete_index[0]])
        # B_drive_cols.remove(item[delete_index[1]])
        # B_drive_cols.remove(item[delete_index[2]])
        # B_drive_cols.remove(item[delete_index[3]])

        move_item_to_start_(B_drive_cols, item)
        # move_item_to_start_(B_drive_cols, [item[tar_index[0]]])
        B_data = B_data[B_drive_cols]
        print("Current B columns {}".format(B_data.columns))

        data1 = A_data.to_numpy()
        data2 = B_data.to_numpy()
    else:
        raise NotImplementedError

    return [data1, data2], labels



