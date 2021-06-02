from decimal import Decimal

# https://4changeenergy.com/tdu-charges
# https://electricityplans.com/texas/tdu-delivery-charges/
TDUS = [
    {
        "name": "AEP Central",
        "ptc_name": "AEP TEXAS CENTRAL COMPANY",
        "charges": [Decimal("4.79"), Decimal("4.27")],
        "rates": [Decimal("0.040272"), Decimal("0.037458")],
    },
    {
        "name": "AEP North",
        "ptc_name": "AEP TEXAS NORTH COMPANY",
        "charges": [Decimal("4.79"), Decimal("3.57")],
        "rates": [Decimal("0.036048"), Decimal("0.030078")],
    },
    {
        "name": "Centerpoint",
        "ptc_name": "CENTERPOINT ENERGY HOUSTON ELECTRIC LLC",
        "charges": [Decimal("4.39")],
        "rates": [Decimal("0.033547"), Decimal("0.032999")],
    },
    {
        "name": "Oncor",
        "ptc_name": "ONCOR ELECTRIC DELIVERY COMPANY",
        "charges": [Decimal("3.42")],
        "rates": [Decimal("0.034928"), Decimal("0.038890")],
    },
    {
        "name": "TNMP",
        "ptc_name": "TEXAS-NEW MEXICO POWER COMPANY",
        "charges": [Decimal("7.85")],
        "rates": [Decimal("0.040403"), Decimal("0.048763")],
    },
]
