# F1 Race Analysis Project

A data analysis pipeline for Formula 1 race data using Python and Power BI.

## Tech Stack
- Python (FastF1, pandas, matplotlib, seaborn)
- Power BI for dashboards

## What it analyses
- Lap time progression per driver
- Tyre degradation by compound
- Fastest lap comparison
- Pit stop strategy
- Season comparison (2023 vs 2024)

## Races covered
- 2023 & 2024 Bahrain Grand Prix
- 2023 & 2024 Monaco Grand Prix

## How to run
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `python main.py`
3. Import CSVs from `data/exports/` into Power BI

## Project Structure
f1_analysis/
├── src/
│   ├── loader.py      # Data loading
│   ├── analysis.py    # Core analysis
│   └── plots.py       # Visualizations
├── data/
│   ├── cache/         # FastF1 cache
│   └── exports/       # CSVs for Power BI
├── main.py
└── requirements.txt