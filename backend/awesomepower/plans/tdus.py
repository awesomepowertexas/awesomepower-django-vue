from decimal import Decimal

# https://4changeenergy.com/tdu-charges
# https://electricityplans.com/texas/tdu-delivery-charges/
TDUS = [
    {
        "name": "AEP Central",
        "ptc_name": "AEP TEXAS CENTRAL COMPANY",
        "charges": [Decimal("5.88"), Decimal("4.79")],
        "rates": [Decimal("0.045174"), Decimal("0.040936")],
    },
    {
        "name": "AEP North",
        "ptc_name": "AEP TEXAS NORTH COMPANY",
        "charges": [Decimal("5.88"), Decimal("4.79")],
        "rates": [Decimal("0.041096"), Decimal("0.041426")],
    },
    {
        "name": "Centerpoint",
        "ptc_name": "CENTERPOINT ENERGY HOUSTON ELECTRIC LLC",
        "charges": [Decimal("4.39")],
        "rates": [Decimal("0.046397"), Decimal("0.046356")],
    },
    {
        "name": "Oncor",
        "ptc_name": "ONCOR ELECTRIC DELIVERY COMPANY",
        "charges": [Decimal("3.42")],
        "rates": [Decimal("0.041114"), Decimal("0.041543")],
    },
    {
        "name": "TNMP",
        "ptc_name": "TEXAS-NEW MEXICO POWER COMPANY",
        "charges": [Decimal("7.85")],
        "rates": [Decimal("0.51602"), Decimal("0.051742")],
    },
]
