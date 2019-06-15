import pandas as pd
import numpy as np
from mes2hb.mes2hb import Mes2Hb

if __name__ == '__main__':
    converter = Mes2Hb()
    df = pd.read_csv('data/sample.csv')

    ir_mes_data = df["CH10"].values
    red_mes_data = df["CH9"].values

    hbo, hb, hbt = converter.convert([red_mes_data, ir_mes_data])
