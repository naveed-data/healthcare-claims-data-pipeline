import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

required_files = ["patients.csv", "providers.csv", "claims.csv"]


def validate_file(file_name):
    file_path = RAW_PATH / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {file_path}")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError(f"{file_name} is empty")

    print(f"{file_name} loaded successfully: {len(df)} rows")
    return df


def main():
    for file_name in required_files:
        df = validate_file(file_name)
        output_path = PROCESSED_PATH / file_name
        df.to_csv(output_path, index=False)

    print("Ingestion completed successfully.")


if __name__ == "__main__":
    main()