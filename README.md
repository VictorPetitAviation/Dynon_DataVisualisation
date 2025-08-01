# Dynon D180 Data Viewer

**Dynon D180 Data Viewer** is a modular Python application designed to parse, segment, and visualize flight data logs from the Dynon D180 flight instrument system. This project is intended for experimental aircraft builders and pilots who wish to analyze engine and flight performance from recorded data.

## ✈️ Project Goals

- **Automatic Parsing** of CSV log files based on Dynon startup events (indicated by column B values).
- **Session Segmentation** into multiple files based on each engine start event.
- **Flexible Visualization** of key engine and flight parameters using customizable graphs.

## 🧩 Architecture Overview

The project is designed to be modular and extensible:

- `parser/` – handles raw CSV ingestion and session segmentation.
- `visualization/` – contains plotting utilities and parameter visualizations.
- `utils/` – helper functions and common operations.
- `data/` – raw and parsed log files.
- `notebooks/` – optional exploratory notebooks (Jupyter).
- `main.py` – CLI or GUI entry point (to be implemented).
- `tests/` – unit tests for each module.

## 🗂️ File Parsing Logic

The parser identifies startup events by scanning **column B** of the input CSV file.
- Each row where column B has a value of `1` marks the beginning of a new flight session.
- The parser splits the file accordingly and stores each session as an individual CSV file in the `data/sessions/` directory.

## 📊 Data Visualization

The visualization module will support plotting the following parameters (list to be extended later):
- Oil Temperature
- Oil Pressure
- RPM
- EGT / CHT
- Battery Voltage
- Altitude and Vertical Speed
- GPS Ground Speed
- G Meter

Each graph will include:
- Time on the X-axis (relative to session start)
- One or more parameters on the Y-axis
- Optional annotations (e.g., takeoff, landing, anomalies)

## ✅ Requirements

- Python 3.8+
- Recommended: virtualenv or poetry

### Core dependencies (to be confirmed and extended):
- `pandas`
- `matplotlib`
- `seaborn` (optional)
- `numpy`
