# Step 1: the question, the ports, the figures

*Draft for Abderrahmane to check, 2026-11-13. Nothing is published yet.*

## The question (proposed)

> **In 2024 Jebel Ali handled its highest container volume since 2015, yet its World Bank port-performance score fell further than almost any other Gulf port. Where did ship time go, and what should a terminal operator look at first?**

Why this one: it is a real question about DP World's home port, it has a clear number behind it, and it connects to what you already know (queues grow fast when a system runs near capacity: your P1 finding).

## The data

| # | Source | What it gives | Checked |
|---|---|---|---|
| 1 | World Bank, 2025. *The Container Port Performance Index 2020 to 2024: Trends and Lessons Learned.* Washington DC. Licence CC BY-NC 3.0 IGO (report p. iv). Data annex: "CPPI 2020 to 2024 Annex.xlsx", 403 ports | Index score per port for 2020-2024, 2024 rank, share of port time spent at berth | Downloaded from the World Bank Open Knowledge Repository; annex rows match the printed table (Jebel Ali p. 63, Khalifa Port p. 64) |
| 2 | DP World press release, 19 Feb 2025, "DP World records highest cargo volumes at Jebel Ali Port since 2015" (dpworld.com) | Jebel Ali 2024: 15.5 million TEU, up 1 million on 2023; capacity 19.4 million TEU a year; achieved "despite challenges like the Red Sea crisis" | Read on dpworld.com |
| 3 | AD Ports Group 2024 annual report (Khalifa Port volume and capacity) | **Not used.** The report's link on adportsgroup.com no longer returns the PDF, and news summaries disagree on the capacity increase (23% vs 33%). No Khalifa Port volume or capacity figure appears in this project | Dropped 2026-11-13 |

## What the index is (you must be able to say this)

- It measures **how long container ships spend in port**: arrival hours (waiting at anchor + sailing in) plus berth hours. Report p. 49.
- Time is compared with the average for ships of the **same size and same number of container moves**, so a big hub is not punished for handling big ships. p. 49.
- The score is the average of two versions of the same idea (an "administrative" and a "statistical" index). p. 48-50.
- **0 = the 2024 world average. Higher = less time in port.** In this edition all five years are measured against the 2024 baseline, so scores can be compared across years (p. 53). In older editions they could not.
- It does **not** say why time is long. p. 52.

## The figures (copied from the annex, nothing changed)

All 12 ports in the World Bank's "Arabian Gulf" maritime region. File: `data/processed/gulf_ports_cppi.csv`, made by `src/extract_gulf.py`.

| Port | Country | 2020 | 2021 | 2022 | 2023 | 2024 | Rank 2024 (of 403) | Berth time as % of port time | Change 2023 to 2024 |
|---|---|---|---|---|---|---|---|---|---|
| **Jebel Ali** | UAE | 102 | 72 | 61 | 73 | **-7** | **262** | 67% | **-80** |
| **Khalifa Port** | UAE | 117 | 131 | 128 | 105 | **46** | 68 | 59% | **-59** |
| **Sharjah** | UAE | n/a | 14 | 17 | 20 | 10 | 155 | 79% | -10 |
| Hamad Port | Qatar | 110 | 138 | 117 | 128 | 125 | 11 | 78% | -3 |
| Salalah | Oman | 141 | 143 | 136 | 141 | 117 | 15 | 64% | -24 |
| Sohar | Oman | 94 | 69 | 56 | 64 | 61 | 48 | 75% | -3 |
| Jubail | Saudi Arabia | 90 | 13 | 34 | 68 | 48 | 64 | 77% | -20 |
| Khalifa Bin Salman | Bahrain | 31 | 53 | 41 | 78 | 46 | 69 | 80% | -32 |
| Dammam | Saudi Arabia | 89 | 104 | 70 | 97 | 9 | 161 | 70% | -88 |
| Shuwaikh | Kuwait | 7 | 9 | 13 | 5 | 13 | 142 | 88% | +8 |
| Shuaiba | Kuwait | 2 | 10 | 18 | 13 | 11 | 146 | 89% | -2 |
| Umm Qasr | Iraq | 1 | 18 | 8 | -6 | -3 | 239 | 79% | +3 |

**Context figures (my calculations from the annex):**
- Of the 387 ports with a score in both years, 214 got worse from 2023 to 2024; the median change was -2. The report says more than half of ports worsened and blames the Red Sea crisis (p. xiv, p. 40).
- Jebel Ali's fall of 80 points was larger than all but 21 of those 387 ports.
- Half of all 403 ports spend 79% or more of port time at berth. Jebel Ali: 67%. Khalifa Port: 59% (only 45 ports are lower). So **about a third of a ship's time at Jebel Ali, and about two-fifths at Khalifa, is spent before the ship is tied up** (waiting and sailing in), against about a fifth at a typical port.
- Jebel Ali ran at about **80% of stated capacity** in 2024 (15.5 / 19.4 million TEU). This is my division of DP World's two published figures, on annual capacity; DP World does not publish a utilisation rate.

## What the data suggests (a hypothesis, not a proven cause)

1. The Gulf's two big UAE hubs lost the most ground in 2024 while small gateway ports barely moved.
2. At both, an unusually large share of ship time is spent **before berthing**. That is consistent with ships waiting for a berth, but it is weak evidence on its own: the figure is a ratio, so a port that works ships quickly at the berth also shows a high share. Salalah has 36% before berth and still ranks 15th. The deck may say "look at berth waiting first", not "waiting is the cause".
3. It happened in the year Jebel Ali's volume hit a nine-year high and Red Sea diversions made ship arrivals less predictable (the report's Singapore case, p. 37, describes exactly this "vessel bunching").

**What we cannot claim:** that volume caused the fall. The index does not give causes, we have no hourly data, and Hamad Port held its score through the same crisis.

## Things worth knowing before an interviewer tells you

- Several news sites reported Jebel Ali as "26th" in this index. The World Bank's own annex says **262nd**. Your deck uses the annex.
- Khor Fakkan and Fujairah are not in the index, so "UAE" here means Jebel Ali, Khalifa Port and Sharjah only.
- The licence is non-commercial with attribution. A student portfolio is fine; every chart must cite the World Bank.
- A DP World interviewer may not enjoy the headline. The deck must be fair: it says the cause is not proven, shows the Red Sea context, and ends with what to check next, not blame.

## Your decisions

1. Is the question right, or do you want a different angle?
2. All 12 Gulf ports, or a shorter list?
3. Who makes the 3 charts: me in Python (fast, consistent), or you in Excel from the CSV (slower, but it is Excel-by-hand practice)?
