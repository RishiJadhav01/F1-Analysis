import os
import fastf1

def setup_cache(cache_path: str = "data/cache"):
    os.makedirs(cache_path, exist_ok=True)
    fastf1.Cache.enable_cache(cache_path)

def load_session(year: int, gp: str, session_type: str = "R"):
    session = fastf1.get_session(year, gp, session_type)
    session.load(laps=True, telemetry=False, weather=False, messages=False)
    return session

def get_driver_laps(session, driver: str):
    laps = session.laps.pick_driver(driver).pick_quicklaps()
    laps = laps[["LapNumber", "LapTime", "Sector1Time", "Sector2Time",
                 "Sector3Time", "Compound", "TyreLife"]].copy()
    laps["LapTimeSec"] = laps["LapTime"].dt.total_seconds()
    laps["Sector1Sec"] = laps["Sector1Time"].dt.total_seconds()
    laps["Sector2Sec"] = laps["Sector2Time"].dt.total_seconds()
    laps["Sector3Sec"] = laps["Sector3Time"].dt.total_seconds()
    return laps