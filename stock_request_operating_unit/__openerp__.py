# -*- coding: utf-8 -*-

{
    "name": "Stock Request Operating Unit",
    "version": "1.0",
    "license": 'AGPL-3',
    "author": "Kitti U.",
    "category": "Warehouse",
    "depends": ["stock_request",
                "operating_unit",
                "stock_operating_unit"],
    "description": """
Stock Request Operating Unit
=========================
Adds a the operating unit to the Stock Request.
    """,
    "data": [
        "views/stock_request_view.xml",
        "security/stock_request_security.xml"
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
}
