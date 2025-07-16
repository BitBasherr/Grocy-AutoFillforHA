#!/usr/bin/env python3

import requests
import time
import json

CONFIG_PATH = "/data/options.json"

with open(CONFIG_PATH) as f:
    cfg = json.load(f)

GROCY_URL = cfg["grocy_url"]
GROCY_API_KEY = cfg["api_key"]
POLL_INTERVAL_SECONDS = cfg["poll_interval"]

print(f"🚀 Grocy Autofill Add-on starting… polling every {POLL_INTERVAL_SECONDS}s")

def get_unknown_products():
    resp = requests.get(
        f"{GROCY_URL}/api/objects/products",
        headers={"GROCY-API-KEY": GROCY_API_KEY},
        timeout=10,
    )
    resp.raise_for_status()
    products = resp.json()
    unknowns = [
        p for p in products if (not p["name"].strip() and p["barcodes"].strip())
    ]
    return unknowns

def lookup_openfoodfacts(barcode):
    resp = requests.get(
        f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json", timeout=10
    )
    if resp.status_code != 200:
        return None
    data = resp.json()
    if data.get("status") != 1:
        return None
    product = data["product"]
    name = product.get("product_name") or product.get("brands") or None
    return name.strip() if name else None

def update_grocy_product(product_id, name):
    resp = requests.put(
        f"{GROCY_URL}/api/objects/products/{product_id}",
        headers={
            "GROCY-API-KEY": GROCY_API_KEY,
            "Content-Type": "application/json",
        },
        json={"name": name},
        timeout=10,
    )
    resp.raise_for_status()
    print(f"✅ Updated product ID {product_id} → {name}")

while True:
    try:
        unknowns = get_unknown_products()
        if unknowns:
            print(f"🔍 Found {len(unknowns)} unknown products to process.")
        for p in unknowns:
            barcode = p["barcodes"].split(",")[0].strip()
            product_id = p["id"]
            print(f"📦 Looking up barcode: {barcode}")
            name = lookup_openfoodfacts(barcode)
            if name:
                update_grocy_product(product_id, name)
            else:
                print(f"❌ No match found for barcode {barcode}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
    time.sleep(POLL_INTERVAL_SECONDS)
