import os

def clean_dynon_csv(input_path, output_path):
    """
    Clean a Dynon D180 CSV file by:
    - Removing the first 5 metadata lines
    - Keeping the 6th line (column headers)
    - Removing the 7th line (Bit Label)
    - Keeping all remaining data rows

    Args:
        input_path (str): Path to the original Dynon CSV file
        output_path (str): Path to save the cleaned CSV
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(input_path, "r", encoding="utf-8", errors="ignore") as infile:
        lines = infile.readlines()

    if len(lines) <= 6:
        raise ValueError("File too short to clean: expected at least 7 lines.")

    # Keep line 5 (header), remove lines 0–4 and line 6
    cleaned_lines = [lines[5]] + lines[7:]

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.writelines(cleaned_lines)

    print(f"[✓] Cleaned file written to: {output_path}")

# For the moment we have to remove some columns to allow the Segmenter to work. It's probably due to the fact that the "CSV' is not "SQUARE"
