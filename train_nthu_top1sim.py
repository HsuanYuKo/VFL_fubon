import os
import sys
from datetime import datetime
import argparse

from model.vertical_fl.Top1SimModel import Top1SimModel
from preprocess.nthu import load_both

now_string = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
os.chdir(sys.path[0] + "/../")  # change working directory
root = "data/nthu/"
A_dataset = root + "Party_A.csv"
B_dataset = root + "Party_B.csv"

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--leak-p', type=float, default=1.0)
parser.add_argument('-g', '--gpu', type=int, default=0)
parser.add_argument('-k', '--top-k', type=int, default=None)
args = parser.parse_args()

num_common_features = 24
[X1, X2], y = load_both(drive_path_A=A_dataset, drive_path_B=B_dataset, active_party='nthu')
name = "nthu_top1sim"

model = Top1SimModel(num_common_features=num_common_features,
                     task='binary_cls',
                     dataset_type='real',
                     blocking_method='knn',
                     metrics=['accuracy', 'r2_score', 'rmse', 'mse'],
                     n_classes=2,
                     grid_min=-10.0,
                     grid_max=10.0,
                     grid_width=1.5,
                     knn_k=50,
                     filter_top_k=args.top_k,
                     kd_tree_radius=0.01,
                     tree_leaf_size=1000,
                     model_name=name + "_" + now_string,
                     val_rate=0.1,
                     test_rate=0.2,
                     drop_key=True, #False代表把common feature放進資料一起練
                     device='cuda:{}'.format(args.gpu),
                     hidden_sizes=[600, 300, 100], #待改
                     train_batch_size=1024 * 4,
                     test_batch_size=1024 * 4,
                     num_epochs=50,
                     learning_rate=1e-2,
                     weight_decay=1e-5,
                     # IMPORTANT: Set num_workers to 0 to prevent deadlock on RTX3090 for unknown reason.
                     num_workers=0 if sys.gettrace() is None else 0,
                     use_scheduler=False, sche_factor=0.1, sche_patience=10, sche_threshold=0.0001,
                     writer_path="runs/{}_{}".format(name, now_string),
                     model_save_path="ckp/{}_{}.pth".format(name, now_string),
                     # SplitNN parameters
                     local_hidden_sizes=[[200], [200]],
                     agg_hidden_sizes=[100],
                     cut_dims=[100, 100],

                     # private link parameters
                     link_epsilon=5e-3,
                     link_delta=5e-3,
                     link_threshold_t=1e-2,
                     sim_leak_p=args.leak_p,
                     link_n_jobs=-1,
                     )
model.train_splitnn(X1, X2, y, data_cache_path="cache/nthu.pkl", scale=True)

