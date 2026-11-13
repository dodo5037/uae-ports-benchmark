"""Three charts from data/processed/gulf_ports_cppi.csv. Run from the repo root.

Chart titles are neutral on purpose: the "so what" goes in the slide title.
Colour: Jebel Ali blue, Khalifa Port orange, every other port grey.
"""
import csv
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SRC = "data/processed/gulf_ports_cppi.csv"
OUT = "outputs/charts/"
BLUE, ORANGE, GREY = "#2a78d6", "#eb6834", "#b4b3ad"
INK, MUTED, SURFACE, GRID = "#0b0b0b", "#52514e", "#fcfcfb", "#e4e3de"
YEARS = [2020, 2021, 2022, 2023, 2024]
WORLD_MEDIAN_BERTH_SHARE = 0.79  # median of all 403 ports in the annex
SOURCE = "Source: World Bank (2025), Container Port Performance Index 2020 to 2024, data annex. CC BY-NC 3.0 IGO."

plt.rcParams.update({"font.family": "Helvetica", "font.size": 11, "axes.edgecolor": GRID,
                     "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
                     "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
                     "xtick.color": MUTED, "ytick.color": MUTED, "text.color": INK})


def num(x):
    return float(x) if x != "" else None


rows = list(csv.DictReader(open(SRC)))
for r in rows:
    r["scores"] = [num(r[f"cppi_{y}"]) for y in YEARS]
    r["change"] = float(r["change_2023_to_2024"])
    r["before_berth"] = 1 - float(r["berth_hours_share_of_port_hours"])


def colour(port):
    return {"Jebel Ali": BLUE, "Khalifa Port": ORANGE}.get(port, GREY)


def finish(fig, ax, title, subtitle, name):
    fig.text(0.02, 0.965, title, fontsize=14, fontweight="bold", ha="left", va="top")
    fig.text(0.02, 0.915, subtitle, fontsize=10.5, color=MUTED, ha="left", va="top")
    fig.text(0.02, 0.015, SOURCE, fontsize=8, color=MUTED, ha="left", va="bottom")
    ax.tick_params(length=0)
    fig.savefig(OUT + name, dpi=200)
    plt.close(fig)
    print("wrote", OUT + name)


# 1. Score by year, all 12 Gulf ports
fig, ax = plt.subplots(figsize=(10, 5.6))
fig.subplots_adjust(left=0.07, right=0.80, top=0.83, bottom=0.11)
for r in sorted(rows, key=lambda r: colour(r["port"]) != GREY):  # grey first, highlights on top
    c = colour(r["port"])
    xs = [y for y, s in zip(YEARS, r["scores"]) if s is not None]
    ys = [s for s in r["scores"] if s is not None]
    ax.plot(xs, ys, color=c, linewidth=2.6 if c != GREY else 1.3, marker="o",
            markersize=6 if c != GREY else 0, zorder=3 if c != GREY else 2)
labels = {"Jebel Ali": (BLUE, 0), "Khalifa Port": (ORANGE, 4), "Hamad Port": (MUTED, 6), "Salalah": (MUTED, -5),
          "Dammam": (MUTED, 8), "Sohar": (MUTED, 6)}
for r in rows:
    if r["port"] in labels:
        c, dy = labels[r["port"]]
        ax.annotate(f'{r["port"]}  {r["scores"][-1]:.0f}', (2024, r["scores"][-1]), xytext=(8, dy),
                    textcoords="offset points", va="center", fontsize=10, color=INK if c in (BLUE, ORANGE) else MUTED,
                    fontweight="bold" if c in (BLUE, ORANGE) else "normal")
ax.axhline(0, color=MUTED, linewidth=0.9, linestyle=(0, (4, 3)), zorder=1)
ax.text(2020, -4, "0 = world average in 2024", fontsize=9, color=MUTED, va="top")
ax.set_ylim(-22, 150)
ax.set_xticks(YEARS)
ax.yaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
ax.set_ylabel("Index score (higher = less ship time in port)", color=MUTED)
finish(fig, ax, "Container port performance score, 12 Gulf ports, 2020 to 2024",
       "Jebel Ali (blue) and Khalifa Port (orange) against the other ten Gulf ports (grey)", "01_score_by_year.png")

# 2. Change 2023 -> 2024
fig, ax = plt.subplots(figsize=(10, 5.6))
fig.subplots_adjust(left=0.20, right=0.95, top=0.83, bottom=0.16)
d = sorted(rows, key=lambda r: r["change"], reverse=True)
ax.barh([r["port"] for r in d], [r["change"] for r in d], color=[colour(r["port"]) for r in d], height=0.62)
for i, r in enumerate(d):
    v = r["change"]
    ax.text(v + (1.5 if v >= 0 else -1.5), i, f"{v:+.0f}", va="center", ha="left" if v >= 0 else "right", fontsize=10,
            color=INK, fontweight="bold" if colour(r["port"]) != GREY else "normal")
ax.axvline(0, color=MUTED, linewidth=0.9)
ax.set_xlim(-100, 20)
ax.xaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
ax.set_xlabel("Change in index score, 2023 to 2024 (points)", color=MUTED)
finish(fig, ax, "Change in port performance score, 2023 to 2024",
       "Across all 387 ports scored in both years, the median change was -2 points", "02_change_2023_2024.png")

# 3. Share of port time spent before the ship is at berth
fig, ax = plt.subplots(figsize=(10, 5.6))
fig.subplots_adjust(left=0.20, right=0.95, top=0.83, bottom=0.16)
d = sorted(rows, key=lambda r: r["before_berth"])
ax.barh([r["port"] for r in d], [100 * r["before_berth"] for r in d], color=[colour(r["port"]) for r in d], height=0.62)
for i, r in enumerate(d):
    ax.text(100 * r["before_berth"] + 0.6, i, f'{100 * r["before_berth"]:.0f}%', va="center", fontsize=10, color=INK,
            bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5),
            fontweight="bold" if colour(r["port"]) != GREY else "normal")
m = 100 * (1 - WORLD_MEDIAN_BERTH_SHARE)
ax.axvline(m, color=MUTED, linewidth=0.9, linestyle=(0, (4, 3)))
ax.text(m + 0.5, -0.75, f"typical port: {m:.0f}% (median of 403)", fontsize=9, color=MUTED, va="center")
ax.set_xlim(0, 48)
ax.set_ylim(-1.1, len(d) - 0.4)
ax.xaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
ax.set_xlabel("Share of a ship's port time spent before it is tied up at the berth, 2024 (%)", color=MUTED)
finish(fig, ax, "Share of port time spent waiting and sailing in, 2024",
       "100% minus the annex column 'Berth hours in % of port hours'", "03_time_before_berth.png")
