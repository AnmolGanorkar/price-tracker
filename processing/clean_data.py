# Data cleaning script
# TODO: Implement data cleaning logic

import pandas as pd

def clean():
    df = pd.read_csv("data/raw_data.csv", encoding='utf-8-sig')

    # remove currency symbol and encoding artifacts
    df["price"] = df["price"].str.replace("£", "").str.replace("Â", "").str.strip()

    # handle missing
    df.dropna(inplace=True)

    # convert to float
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    df.dropna(inplace=True)

    # remove duplicates
    df.drop_duplicates(inplace=True)

    df.to_csv("data/cleaned_data.csv", index=False)

    print("Cleaning Done")

if __name__ == "__main__":
    clean()