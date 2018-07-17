import pandas as pd
import numpy as np
import datetime
import math
import statistics
import time
import sklearn
import glob, os

# ----------------------------
# データの読み込み
# ----------------------------
print(os.getcwd())
path_dataset_main = "./data/csv/"
path_save_data = "./data/save_data/"

list_data_csv_name_main = [os.path.basename(r) for r in glob.glob(path_dataset_main + '*')]
print(list_data_csv_name_main)

list_df = []
for i in range(len(list_data_csv_name_main)):
    list_df.append(pd.read_csv(path_dataset_main + list_data_csv_name_main[i]))
    print(list_data_csv_name_main[i], " --> len:", len(list_df[i]), ", columns:", list_df[i].columns)

    for col in list_df[i].columns:
        print("  name_col:", col, " > n_uniq:", len(list_df[i][col].unique()))
