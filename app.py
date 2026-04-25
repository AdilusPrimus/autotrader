from flask import Flask, render_template, request
from ImportCarRequests import fetch_listings, DEFAULT_PARAMS

app = Flask(__name__)


def _int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _process_listing(i, listing):
    pricing = listing.get('pricingDetail') or {}
    specs = listing.get('specifications') or {}
    mileage = specs.get('mileage') or {}

    nav = any('nav' in f.lower() for f in listing.get('features', []))

    mileage_str = ''
    if mileage:
        unit = 'km' if mileage.get('label') != 'miles' else 'mi'
        mileage_str = f"{mileage.get('value', '')} {unit}"

    return {
        'num': i,
        'id': listing.get('id', ''),
        'year': listing.get('year', ''),
        'make': listing.get('make', ''),
        'model': listing.get('model', ''),
        'title': listing.get('title', ''),
        'nav': nav,
        'mileage': mileage_str,
        'incentive': pricing.get('incentive'),
        'sale_price': pricing.get('salePrice'),
        'price_valid_until': listing.get('priceValidUntil', ''),
        'vin': listing.get('vin', ''),
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    form = dict(DEFAULT_PARAMS)
    listings = None
    error = None

    if request.method == 'POST':
        form = {
            'zip': request.form.get('zip', DEFAULT_PARAMS['zip']),
            'makeCodeList': request.form.get('makeCodeList', DEFAULT_PARAMS['makeCodeList']),
            'modelCodeList': request.form.get('modelCodeList', DEFAULT_PARAMS['modelCodeList']),
            'marketExtension': 'true',
            'startYear': _int(request.form.get('startYear'), DEFAULT_PARAMS['startYear']),
            'endYear': _int(request.form.get('endYear'), DEFAULT_PARAMS['endYear']),
            'maxMileage': _int(request.form.get('maxMileage'), DEFAULT_PARAMS['maxMileage']),
            'maxPrice': _int(request.form.get('maxPrice'), DEFAULT_PARAMS['maxPrice']),
            'searchRadius': _int(request.form.get('searchRadius'), DEFAULT_PARAMS['searchRadius']),
            'style': request.form.get('style', DEFAULT_PARAMS['style']),
            'sortBy': request.form.get('sortBy', DEFAULT_PARAMS['sortBy']),
            'numRecords': _int(request.form.get('numRecords'), DEFAULT_PARAMS['numRecords']),
            'firstRecord': 0,
        }
        try:
            raw = fetch_listings(form)
            listings = [_process_listing(i + 1, l) for i, l in enumerate(raw)]
        except Exception as e:
            error = str(e)

    return render_template('index.html', form=form, listings=listings, error=error)


if __name__ == '__main__':
    app.run(debug=True)
