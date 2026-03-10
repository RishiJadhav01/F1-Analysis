import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")

def plot_lap_times(combined_df):

    fig, ax = plt.subplots(figsize=(14, 6))
    for driver, group in combined_df.groupby("Driver"):
        ax.plot(group["LapNumber"], group["LapTimeSec"],
                label=driver, marker="o", markersize=3, linewidth=1.5)
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time (seconds)")
    ax.set_title("Lap Time Progression by Driver")
    ax.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig("data/exports/lap_times_chart.png", dpi=150)
    plt.show()
    print("Saved: data/exports/lap_times_chart.png")

def plot_tyre_degradation(deg_df):

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=deg_df, x="TyreLife", y="LapTimeSec",
                 hue="Compound", ax=ax, linewidth=2)
    ax.set_title("Tyre Degradation by Compound")
    ax.set_xlabel("Tyre Age (laps)")
    ax.set_ylabel("Average Lap Time (seconds)")
    plt.tight_layout()
    plt.savefig("data/exports/tyre_degradation_chart.png", dpi=150)
    plt.show()
    print("Saved: data/exports/tyre_degradation_chart.png")

def plot_sector_heatmap(combined_df):

    pivot = combined_df.groupby("Driver")[["Sector1Sec", "Sector2Sec", "Sector3Sec"]].min()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(pivot, annot=True, fmt=".2f", cmap="RdYlGn_r",
                ax=ax, linewidths=0.5)
    ax.set_title("Best Sector Times by Driver (seconds)")
    ax.set_xticklabels(["Sector 1", "Sector 2", "Sector 3"])
    plt.tight_layout()
    plt.savefig("data/exports/sector_heatmap.png", dpi=150)
    plt.show()
    print("Saved: data/exports/sector_heatmap.png")

def plot_fastest_laps(summary_df):

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(summary_df["Driver"], summary_df["Fastest Lap (s)"], color="tomato")
    ax.set_xlabel("Fastest Lap (seconds)")
    ax.set_title("Fastest Lap Comparison")
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig("data/exports/fastest_laps_chart.png", dpi=150)
    plt.show()
    print("Saved: data/exports/fastest_laps_chart.png")