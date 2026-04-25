# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python script that queries the autotrader.com search REST API (`https://www.autotrader.com/rest/searchresults/base`) without requiring an account and prints matching car listings to stdout.

## Setup

```bash
python3 -m venv .venv
. ./.venv/bin/activate
pip install --upgrade pip
pip install requests flask
```

## Running the Script

```bash
python3 ./ImportCarRequests.py
```

No arguments — all search parameters are hardcoded in the `params` dict near the top of `ImportCarRequests.py`. Edit that dict to change the search (zip, make/model codes, year range, price, mileage, radius, etc.).

## Architecture

The entire project is a single script (`ImportCarRequests.py`). It:

1. Builds a query using the `params` dict and sends a GET request with a browser-spoofing `User-Agent` header (required — autotrader.com blocks non-browser agents).
2. Parses the JSON response and iterates `data['listings']`.
3. For each listing prints: counter, listing ID, nav feature presence (`NAV`/`---`), year, mileage, incentive price, `priceValidUntil` date, sale price, and VIN.

`ResponseTemplate.json` is a reference sample of a single listing object from the API — useful for understanding all available fields without making a live request. Key fields used by the script:

- `listing['id']`, `listing['year']`, `listing['vin']`
- `listing['features']` — list of feature strings; nav detection does a case-insensitive `'nav' in feature`
- `listing['specifications']['mileage']['value']` and `['label']`
- `listing['pricingDetail']['incentive']` and `['salePrice']`
- `listing['priceValidUntil']`

## Known Issues / TODOs

- Search parameters are hardcoded; the TODO comment in the script calls for externalizing them (e.g., CLI args or a config file).
- Mileage threshold comparison (`listing['specifications']['mileage']['value'] < "300000"`) is a **string comparison**, not numeric — will produce incorrect results for values whose string sort order differs from numeric order.
- The `hasnav` flag is never reset between listings, so once a listing has nav, all subsequent listings will also show `NAV`.
- The `.vscode/launch.json` includes a Flask configuration (`FLASK_APP=app.py`) indicating a planned web front-end that does not yet exist.
