# -*- coding: utf-8 -*-
{
    "name": "PABI Asset Management Operating Unit",
    "version": "1.0",
    "license": 'AGPL-3',
    "author": "Kitti U.",
    "category": "Asset Management",
    "depends": ["pabi_asset_management",
                "operating_unit",
                ],
    "description": """
Adds a the operating unit to

- Asset Request
- Asset Change Owner
- Asset Transfer
    """,
    "data": [
        "views/asset_request_view.xml",
        "views/asset_changeowner_view.xml",
        "views/asset_transfer_view.xml",
        "security/asset_request_security.xml",
        "security/asset_changeowner_security.xml",
        "security/asset_transfer_security.xml",
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
}
