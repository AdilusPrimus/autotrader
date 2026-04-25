import argparse
import requests

URL = 'https://www.autotrader.com/rest/searchresults/base'

HEADERS = {
    'Cache-Control': 'no-cache',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

DEFAULT_PARAMS = dict(
    zip=90210,
    makeCodeList='ROV',
    modelCodeList='DEFEND',
    marketExtension='true',
    maxMileage=500000,
    startYear=1953,
    endYear=2016,
    searchRadius=10000,
    maxPrice=500000,
    sortBy='mileageASC',
    numRecords=1000,
    firstRecord=0,
    style='Truck'
)


def fetch_listings(params):
    resp = requests.get(url=URL, params=params, headers=HEADERS)
    data = resp.json()
    return data.get('listings', [])


def _has_nav(listing):
    return any('nav' in f.lower() for f in listing.get('features', []))


def _mileage(listing):
    specs = listing.get('specifications', {}) or {}
    if 'mileage' not in specs:
        return None, None
    raw = specs['mileage']
    value_str = raw.get('value', '').replace(',', '')
    try:
        if int(value_str) >= 300000:
            return None, None
    except ValueError:
        return None, None
    unit = 'km' if raw.get('label') != 'miles' else 'mi'
    return value_str, unit


def print_listing(counter, listing):
    pricing = listing.get('pricingDetail') or {}
    value_str, unit = _mileage(listing)
    mileage_col = f"{value_str} {unit}" if value_str else '----------'
    incentive = pricing.get('incentive')
    incentive_col = f"{incentive}$" if incentive is not None else ''
    sale = pricing.get('salePrice')
    sale_col = f"{sale}$" if sale is not None else '------$'
    nav_col = 'NAV' if _has_nav(listing) else '---'
    vin = listing.get('vin', '-----------------')
    price_until = listing.get('priceValidUntil', '')

    print(f"{counter}\t{listing['id']}\t{nav_col}\t{listing['year']}\t"
          f"{mileage_col}\t{incentive_col}\t{price_until}\t{sale_col}\t{vin}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search autotrader.com listings')
    parser.add_argument('--zip', default=DEFAULT_PARAMS['zip'])
    parser.add_argument('--make', dest='makeCodeList', default=DEFAULT_PARAMS['makeCodeList'], metavar='CODE')
    parser.add_argument('--model', dest='modelCodeList', default=DEFAULT_PARAMS['modelCodeList'], metavar='CODE')
    parser.add_argument('--start-year', dest='startYear', type=int, default=DEFAULT_PARAMS['startYear'])
    parser.add_argument('--end-year', dest='endYear', type=int, default=DEFAULT_PARAMS['endYear'])
    parser.add_argument('--max-mileage', dest='maxMileage', type=int, default=DEFAULT_PARAMS['maxMileage'])
    parser.add_argument('--max-price', dest='maxPrice', type=int, default=DEFAULT_PARAMS['maxPrice'])
    parser.add_argument('--radius', dest='searchRadius', type=int, default=DEFAULT_PARAMS['searchRadius'])
    parser.add_argument('--style', default=DEFAULT_PARAMS['style'])
    parser.add_argument('--sort', dest='sortBy', default=DEFAULT_PARAMS['sortBy'],
                        choices=['mileageASC', 'mileageDESC', 'priceASC', 'priceDESC',
                                 'yearASC', 'yearDESC', 'relevance'])
    parser.add_argument('--num-records', dest='numRecords', type=int, default=DEFAULT_PARAMS['numRecords'])

    args = parser.parse_args()
    params = {**DEFAULT_PARAMS, **vars(args)}

    listings = fetch_listings(params)

    if not listings:
        print('NO MATCH FOUND')
    else:
        for i, listing in enumerate(listings, 1):
            print_listing(i, listing)
