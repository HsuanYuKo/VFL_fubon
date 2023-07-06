import pandas as pd
import random
from utils import move_item_to_start_, move_item_to_end_

#item = ['LIMIT_BAL', 'SEX','EDUCATION','MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1']
#item = ['ID','LIMIT_BAL', 'SEX','EDUCATION','MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT1','BILL_AMT2','BILL_AMT3']
item = ['LIMIT_BAL', 'SEX']
# index = [0, 1, 2, 3, 4]
def load_credit_card(credit_card_path):
    print("Loading credit_card from {}".format(credit_card_path))
    credit_card_data = pd.read_csv(credit_card_path)
    # credit_card_data.drop(columns=['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE'])
    credit_card_data.info(verbose=True)

    labels = credit_card_data['default payment next month'].to_numpy()
    credit_card_data = credit_card_data.drop(columns=['default payment next month']).to_numpy()

    return credit_card_data, labels


def load_both(credit_card_path_A, credit_card_path_B, active_party='credit_card'):
    print("Loading A from {}".format(credit_card_path_A))
    A_data = pd.read_csv(credit_card_path_A)
    print("Loading B from {}".format(credit_card_path_B))
    B_data = pd.read_csv(credit_card_path_B)
    # tar_index = random.sample(index, 1)

    if active_party == 'credit_card':
        labels = A_data['default payment next month'].to_numpy()
        A_data.drop(columns=['default payment next month'], inplace=True)

        # move lon and lat to end
        A_credit_card_cols = list(A_data.columns)
        A_data = A_data[A_credit_card_cols]
        move_item_to_end_(A_credit_card_cols, item)
        # move_item_to_end_(A_credit_card_cols, [item[tar_index[0]]])
        A_data = A_data[A_credit_card_cols]
        print("Current A columns {}".format(A_data.columns))

        # B_data.drop(columns=['school_name'], inplace=True)

        # move lon and lat to start
        B_credit_card_cols = list(B_data.columns)
        # delete_index = [x for x in index if x not in tar_index]
        # B_credit_card_cols.remove(item[delete_index[0]])
        # B_credit_card_cols.remove(item[delete_index[1]])
        # B_credit_card_cols.remove(item[delete_index[2]])
        # B_credit_card_cols.remove(item[delete_index[3]])
   

        move_item_to_start_(B_credit_card_cols, item)
        # move_item_to_start_(B_credit_card_cols, [item[tar_index[0]]])
        B_data = B_data[B_credit_card_cols]
        print("Current B columns {}".format(B_data.columns))

        # print("Current common feature columns {}".format([item[tar_index[0]]]))
        data1 = A_data.to_numpy()
        data2 = B_data.to_numpy()
    else:
        raise NotImplementedError

    return [data1, data2], labels



