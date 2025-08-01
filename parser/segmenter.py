import os
import pandas as pd

def parse_and_split_sessions(input_path, output_dir, boot_column="boot"):
    """
    Parse a cleaned Dynon D180 CSV file and split it into flight sessions
    based on values of 1 in the 'boot' column.

    Args:
        input_path (str): Path to the cleaned CSV file (after running cleaner.py).
        output_dir (str): Directory where session CSVs will be saved.
        boot_column (str): Name of the column used to detect session start (default: 'boot').
    """
    os.makedirs(output_dir, exist_ok=True)

    print(f"[INFO] Reading file: {input_path}")
    df = pd.read_csv(input_path, sep=";", low_memory=False)

    # Clean and convert the boot column
    df[boot_column] = (
        df[boot_column]
        .astype(str)
        .str.strip()
        .str.replace(',', '.', regex=False)
        .replace('', '0')
    )
    df[boot_column] = pd.to_numeric(df[boot_column], errors='coerce').fillna(0).astype(int)

    # Find session start indices
    start_indices = df.index[df[boot_column] == 1].tolist()
    if not start_indices:
        print("[!] No boot == 1 found in the file.")
        return

    # Add end of file index
    start_indices.append(len(df))

    print(f"[✓] Found {len(start_indices) - 1} session(s).")

    # Write each session to its own CSV
    for i in range(len(start_indices) - 1):
        session_df = df.iloc[start_indices[i]:start_indices[i+1]].copy()
        session_path = os.path.join(output_dir, f"session_{i+1}.csv")
        session_df.to_csv(session_path, sep=";", index=False)
        print(f"[✓] Session {i+1} saved to: {session_path}")
