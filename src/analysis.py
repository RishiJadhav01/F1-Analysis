import pandas as pd
from src.loader import get_driver_laps

def compare_drivers(session, drivers: list):
    all_laps = []
    for driver in drivers:
        df = get_driver_laps(session, driver)
        df["Driver"] = driver
        all_laps.append(df)
    return pd.concat(all_laps, ignore_index=True)

def tyre_degradation(driver_laps: pd.DataFrame):
    return (
        driver_laps.groupby(["Compound", "TyreLife"])["LapTimeSec"]
        .mean()
        .reset_index()
    )

def best_sector_times(driver_laps: pd.DataFrame):
    s1 = driver_laps["Sector1Sec"].min()
    s2 = driver_laps["Sector2Sec"].min()
    s3 = driver_laps["Sector3Sec"].min()
    theoretical = s1 + s2 + s3
    return {
        "Best S1 (s)": round(s1, 3),
        "Best S2 (s)": round(s2, 3),
        "Best S3 (s)": round(s3, 3),
        "Theoretical Best Lap (s)": round(theoretical, 3)
    }

def driver_summary(session, drivers: list):
    rows = []
    for driver in drivers:
        laps = get_driver_laps(session, driver)
        if laps.empty:
            continue
        rows.append({
            "Driver": driver,
            "Fastest Lap (s)": round(laps["LapTimeSec"].min(), 3),
            "Avg Lap (s)": round(laps["LapTimeSec"].mean(), 3),
            "Laps Completed": len(laps),
            "Best S1 (s)": round(laps["Sector1Sec"].min(), 3),
            "Best S2 (s)": round(laps["Sector2Sec"].min(), 3),
            "Best S3 (s)": round(laps["Sector3Sec"].min(), 3),
        })
    return pd.DataFrame(rows).sort_values("Fastest Lap (s)")

def pit_stop_analysis(session):
    laps = session.laps[["Driver", "LapNumber", "Stint", "Compound", "TyreLife", "PitInTime", "PitOutTime"]].copy()
    pit_laps = laps[laps["PitInTime"].notna()][["Driver", "LapNumber", "Stint", "Compound"]].copy()
    pit_laps.columns = ["Driver", "PitLap", "Stint", "Compound"]
    return pit_laps