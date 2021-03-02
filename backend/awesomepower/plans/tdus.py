from decimal import Decimal

# https://4changeenergy.com/tdu-charges
# https://electricityplans.com/texas/tdu-delivery-charges/
TDUS = [
    {
        "name": "AEP Central",
        "ptc_name": "AEP TEXAS CENTRAL COMPANY",
        "charges": [Decimal("4.27")],
        "rates": [Decimal("0.037458"), Decimal("0.042929")],
    },
    {
        "name": "AEP North",
        "ptc_name": "AEP TEXAS NORTH COMPANY",
        "charges": [Decimal("3.57")],
        "rates": [Decimal("0.030078"), Decimal("0.035325")],
    },
    {
        "name": "Centerpoint",
        "ptc_name": "CENTERPOINT ENERGY HOUSTON ELECTRIC LLC",
        "charges": [Decimal("4.39")],
        "rates": [Decimal("0.032999"), Decimal("0.042723")],
    },
    {
        "name": "Oncor",
        "ptc_name": "ONCOR ELECTRIC DELIVERY COMPANY",
        "charges": [Decimal("3.42")],
        "rates": [Decimal("0.034926"), Decimal("0.038890")],
    },
    {
        "name": "TNMP",
        "ptc_name": "TEXAS-NEW MEXICO POWER COMPANY",
        "charges": [Decimal("7.85")],
        "rates": [Decimal("0.040403"), Decimal("0.048763")],
    },
]
