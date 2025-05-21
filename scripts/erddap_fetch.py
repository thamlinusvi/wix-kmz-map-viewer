#!/usr/bin/env python3
# File: scripts/erddap_fetch.py

import os
import json
from erddapy import ERDDAP

DATASETS = [
    "uvi_01-20230921T1324-trajectory-raw-delayed",
    "uvi_01-20241026T1158-trajectory-raw-rt",
    "uvi_01-20240828T1337-trajectory-raw-rt",
    "uvi_01-20241004T1402-trajectory-raw-rt",
    "uvi_01-20240809T1334-trajectory-raw-rt",
    "uvi_01-20250318T2008-trajectory-raw-rt",
    "uvi_02-20231102T1447-trajectory-raw-delayed",
    "uvi_02-20241105T1313-trajectory-raw-rt",
    "uvi_02-20250211T1347-trajectory-raw-rt",
    "uvi_02-20250306T1911-trajectory-raw-rt"
]

def fetch_and_save(dataset_id):
    print(f"Fetching {dataset_id}...")
    e = ERDDAP(
        server="https://slocum-data.marine.rutgers.edu/erddap",
        protocol="tabledap",
    )

    e.dataset_id = dataset_id
    e.response = "geoJson"
    e.variables = ["time", "latitude", "longitude"]
    e.order_by = ["time"]

    try:
        geojson = e.to_geojson()
        output_dir = "data"
        os.makedirs(output_dir, exist_ok=True)
        with open(f"{output_dir}/{dataset_id}.geojson", "w") as f:
            json.dump(geojson, f)
        print(f"✔ Saved {dataset_id}.geojson")
    except Exception as ex:
        print(f"✖ Failed {dataset_id}: {ex}")

if __name__ == "__main__":
    for ds in DATASETS:
        fetch_and_save(ds)
