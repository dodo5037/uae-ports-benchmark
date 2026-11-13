"""Pull the Gulf ports out of the World Bank CPPI 2020-2024 annex into a small CSV.

Source file: data/raw/worldbank/CPPI_2020_to_2024_Annex.xlsx (World Bank, 2025, CC BY-NC 3.0 IGO).
Nothing is changed: values are copied as published. Run from the repo root.
"""
import csv
import sys
import openpyxl

SRC = "data/raw/worldbank/CPPI_2020_to_2024_Annex.xlsx"
OUT = "data/processed/gulf_ports_cppi.csv"
PORTS = ["Jebel Ali", "Khalifa Port", "Sharjah", "Hamad Port", "Dammam", "Jubail",
         "Khalifa Bin Salman", "Sohar", "Salalah", "Shuwaikh", "Shuaiba", "Umm Qasr"]

rows = list(openpyxl.load_workbook(SRC, read_only=True, data_only=True)["Annex"].iter_rows(values_only=True))
head, body = rows[0], rows[1:]
by_name = {r[0]: r for r in body}
missing = [p for p in PORTS if p not in by_name]
if missing:
    sys.exit(f"not in annex: {missing}")

with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["port", "locode", "territory", "cppi_2020", "cppi_2021", "cppi_2022", "cppi_2023", "cppi_2024",
                "rank_2024_of_403", "berth_hours_share_of_port_hours", "change_2023_to_2024"])
    for p in PORTS:
        r = by_name[p]
        w.writerow([r[0], r[1], r[2], *r[9:14], r[14], r[15], r[13] - r[12]])
print(f"{len(PORTS)} ports -> {OUT}; annex has {len(body)} ports")
