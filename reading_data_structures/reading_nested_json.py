import json

import numpy as np
import pandas as pd
from pandas.io import json as pd_json


def read_json_by_json_normalize():
    with open("C:\\Users\\spoch\\repos\\pandas_playground\\reading_data_structures\\data_files\\nested_data.json") as file:
        data_dict = json.load(file)

    df = pd_json.json_normalize(data_dict)
    df.columns = df.columns.map(lambda x: x.split('.')[-1])

    lens_1 = np.array([len(item) for item in df['data_1']])
    resulting_df = pd.DataFrame(
        {'data_1': np.concatenate(df['data_1'].values),
         'data_2': np.concatenate(df['data_2'].values),
         'category_1': np.repeat(df['category_1'].values, lens_1),
         'category_2': np.repeat(df['category_2'].values, lens_1),
         'category_3': np.repeat(df['category_3'].values, lens_1)
         }
    )

    print(resulting_df.head())


def read_json_by_orient_index():
    with open("C:\\Users\\spoch\\repos\\pandas_playground\\reading_data_structures\\data_files\\nested_data.json") as file:
        data_dict = json.load(file)

    df = pd.DataFrame.from_dict(data_dict, orient='index')

    print(df.head())


if __name__ == '__main__':
    read_json_by_json_normalize()
    read_json_by_orient_index()
