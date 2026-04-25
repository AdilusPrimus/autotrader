# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project that queries the autotrader.com search REST API (`https://www.autotrader.com/rest/searchresults/base`) without requiring an account. It has two interfaces: a CLI script and a Flask web UI.

## Setup

```bash
python3 -m venv .venv
. ./.venv/bin/activate
pip install --upgrade pip
pip install requests flask
```

## Running

**CLI:**
```bash
python3 ./ImportCarRequests.py
# Override any default parameter:
python3 ./ImportCarRequests.py --zip 90210 --make ROV --model DEFEND --start-year 1980 --end-year 2013 --max-price 100000 --radius 500 --sort priceASC
```

**Flask web UI:**
```bash
flask --app app.py run --debug
# then open http://127.0.0.1:5000
```

## Architecture

`ImportCarRequests.py` is the core module. It exposes two things used by both the CLI and the web app:

- `DEFAULT_PARAMS` — dict of all search parameters with default values
- `fetch_listings(params)` — makes the GET request and returns `data['listings']` (empty list on no match)

The script requires a browser-spoofing `User-Agent` header — autotrader.com blocks requests without one.

`app.py` imports `fetch_listings` and `DEFAULT_PARAMS` from `ImportCarRequests`, processes each raw listing into a flat display dict via `_process_listing()`, and passes it to `templates/index.html`.

`ResponseTemplate.json` is a reference sample of a single listing object from the API — useful for understanding available fields without making a live request. Key fields:

- `listing['id']`, `listing['year']`, `listing['vin']`, `listing['make']`, `listing['model']`
- `listing['features']` — list of feature strings; nav detection checks `'nav' in feature.lower()`
- `listing['specifications']['mileage']['value']` (comma-formatted string) and `['label']`
- `listing['pricingDetail']['incentive']` and `['salePrice']`
- `listing['priceValidUntil']`

## Known Issues / TODOs

- The Flask web UI does not paginate results; large `numRecords` values return everything at once.
- Make/model codes (`makeCodeList`, `modelCodeList`) are autotrader-internal identifiers (e.g. `ROV` for Land Rover, `DEFEND` for Defender) — there is no lookup helper yet.
