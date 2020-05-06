from dbfread import DBF
import os
import pandas as pd


def converter_para_csv(path_dados, join_dfs=False):
    new_path = path_dados + "_CSV"
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    files = [os.path.join(path_dados, file) for file in os.listdir(path_dados)]

    dfs = []

    for file in files:
        rec = DBF(file, load=True, encoding='Latin-1').records
        df = pd.DataFrame(rec)
        new_file = os.path.split(file)[-1][:-3] + 'csv'
        new_f_path = os.path.join(new_path, new_file)
        df.to_csv(new_f_path, sep=';', encoding='Latin-1')
        print(f'Arquivo salvo em {new_f_path}')
        if join_dfs:
            dfs.append(df)
    if join_dfs:
        return pd.concat(dfs)

if __name__ == '__main__':

    converter_para_csv('SIM_SP')