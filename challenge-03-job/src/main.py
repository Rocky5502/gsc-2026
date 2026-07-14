import pandas as pd

def main():
    print("Starting Job Failure Prediction baseline...")

    try:
        df = pd.read_csv("../data/train.csv")
        print("Data loaded successfully!")
        print(df.head())
        print("\nBasic stats:")
        print(df.describe())
    except Exception as e:
        print("Error loading data:", e)

if __name__ == "__main__":
    main()
