import pickle

import pandas as pd


def get_prediction(data: pd.DataFrame) -> float:
    with open('src/pipeline.pkl', 'rb') as file:
        pipline = pickle.load(file)

    return pipline.predict(data)[0]
