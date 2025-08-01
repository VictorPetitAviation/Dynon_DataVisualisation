import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

def plot_oil_temperature(session_path, time_column="Label", temp_column="oil temp"):
    """
    Plot oil temperature (°F) vs time (hh:mm:ss) for a flight session.
    Adds time markers and temperature thresholds with custom colors.

    Args:
        session_path (str): Path to the session CSV file
        time_column (str): Column representing time (e.g., 'Label')
        temp_column (str): Column with oil temperature in °F
    """
    if not os.path.isfile(session_path):
        print(f"[!] File not found: {session_path}")
        return

    df = pd.read_csv(session_path, sep=";", low_memory=False)

    # Clean and convert relevant columns
    for col in [time_column, temp_column]:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.replace(",", ".", regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.dropna(subset=[time_column, temp_column], inplace=True)

    # Temps relatif en secondes
    time_sec = df[time_column] - df[time_column].iloc[0]
    df["elapsed_sec"] = time_sec
    df["time_str"] = time_sec.apply(lambda x: str(timedelta(seconds=int(x))))

    # Plot setup
    plt.figure(figsize=(12, 6))
    plt.plot(df["elapsed_sec"], df[temp_column], label="Oil Temp (°F)", color="black")

    # Thresholds: value → (label, color)
    thresholds = {
        180: ("180°F (min croisière)", "green"),
        200: ("200°F (zone normale)", "orange"),
        245: ("245°F (max recommandé)", "red")
    }

    for value, (label, color) in thresholds.items():
        plt.axhline(y=value, color=color, linestyle="-", linewidth=1.2, label=label)

    # Vertical markers every 5 min
    max_sec = int(df["elapsed_sec"].max())
    for sec in range(300, max_sec + 1, 300):
        plt.axvline(x=sec, color="gray", linestyle=":", linewidth=0.5)

    # Format x-axis ticks to hh:mm:ss
    tick_positions = df["elapsed_sec"][::max(1, len(df)//10)]
    tick_labels = df["time_str"][::max(1, len(df)//10)]
    plt.xticks(tick_positions, tick_labels, rotation=45)

    # Final plot styling
    plt.xlabel("Time since session start (hh:mm:ss)")
    plt.ylabel("Oil Temperature (°F)")
    plt.title("Oil Temperature vs Time")
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()
