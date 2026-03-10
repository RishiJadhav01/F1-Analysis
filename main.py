import os
from src.loader import setup_cache, load_session, get_driver_laps
from src.analysis import compare_drivers, tyre_degradation, driver_summary, pit_stop_analysis


# races to analyse
RACES = [
    {"year": 2023, "gp": "Bahrain", "session": "R"},
    {"year": 2024, "gp": "Bahrain", "session": "R"},
    {"year": 2023, "gp": "Monaco", "session": "R"},
    {"year": 2024, "gp": "Monaco", "session": "R"},
]
DRIVERS = ["VER", "LEC", "HAM", "NOR", "SAI", "PER", "RUS", "ALO"]

setup_cache()
os.makedirs("data/exports", exist_ok=True)

all_laps = []
all_summaries = []
all_pit_stops = []

for race in RACES:
    print(f"\nLoading {race['year']} {race['gp']} Grand Prix...")
    session = load_session(race["year"], race["gp"], race["session"])

    combined = compare_drivers(session, DRIVERS)
    combined["Year"] = race["year"]
    combined["GP"] = race["gp"]
    all_laps.append(combined)

    summary = driver_summary(session, DRIVERS)
    summary["Year"] = race["year"]
    summary["GP"] = race["gp"]
    all_summaries.append(summary)

    pits = pit_stop_analysis(session)
    pits["Year"] = race["year"]
    pits["GP"] = race["gp"]
    all_pit_stops.append(pits)

import pandas as pd

print("\nExporting CSVs...")
pd.concat(all_laps).to_csv("data/exports/lap_times.csv", index=False)
pd.concat(all_summaries).to_csv("data/exports/driver_summary.csv", index=False)
pd.concat(all_pit_stops).to_csv("data/exports/pit_stops.csv", index=False)

print("\n Done! All 4 races exported to data/exports/")