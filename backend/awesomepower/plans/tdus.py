from decimal import Decimal

# https://4changeenergy.com/tdu-charges
# https://electricityplans.com/texas/tdu-delivery-charges/
TDUS = [
    {
        "name": "AEP Central",
        "ptc_name": "AEP TEXAS CENTRAL COMPANY",
        "charges": [Decimal("5.88"), Decimal("4.79"), Decimal("4.27")],
        "rates": [Decimal("0.040936"), Decimal("0.045504")],
    },
    {
        "name": "AEP North",
        "ptc_name": "AEP TEXAS NORTH COMPANY",
        "charges": [Decimal("5.88"), Decimal("4.79"), Decimal("3.57")],
        "rates": [Decimal("0.041426"), Decimal("0.036048")],
    },
    {
        "name": "Centerpoint",
        "ptc_name": "CENTERPOINT ENERGY HOUSTON ELECTRIC LLC",
        "charges": [Decimal("4.39")],
        "rates": [Decimal("0.045727"), Decimal("0.046029")],
    },
    {
        "name": "Oncor",
        "ptc_name": "ONCOR ELECTRIC DELIVERY COMPANY",
        "charges": [Decimal("3.42")],
        "rates": [Decimal("0.041543"), Decimal("0.034928")],
    },
    {
        "name": "TNMP",
        "ptc_name": "TEXAS-NEW MEXICO POWER COMPANY",
        "charges": [Decimal("7.85")],
        "rates": [Decimal("0.51602"), Decimal("0.051742")],
    },
]
