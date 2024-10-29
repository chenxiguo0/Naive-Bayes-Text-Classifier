import pandas as pd
from pathlib import Path

def build_dataframe(folder):
        path = Path(folder)
        df_train = pd.DataFrame(columns=["author"])
        df_test = pd.DataFrame(columns=["author"])
        author_to_id_map = {"kennedy": 0, "johnson": 1}

        def make_df_from_dir(dir_name, df):
            for f in path.glob(f"../data/{dir_name}/*.txt"):
                with open(f) as fp:
                    text = fp.read()
                    if dir_name in ("kennedy", "johnson"):
                        new_row = pd.DataFrame({"author": [dir_name], "text": [text]})
                        df = pd.concat([df, new_row], ignore_index=True)
                    else:
                        file_name = Path(f).stem
                        new_row = pd.DataFrame({"author": [file_name.split('_')[2]], "text": [text]})
                        df = pd.concat([df, new_row], ignore_index=True)
            return df

        for p in path.iterdir():
            if p.name in ("kennedy", "johnson"):
                df_train = make_df_from_dir(p.name, df_train)
            elif p.name == "unlabeled":
                df_test = make_df_from_dir(p.name, df_test)

        df_train["author"] = df_train["author"].apply(lambda x: author_to_id_map.get(x))
        df_test["author"] = df_test["author"].apply(lambda x: author_to_id_map.get(x))
        return df_train, df_test

