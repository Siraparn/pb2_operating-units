# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Purchase Request to Call for Bids with Operating Units",
    "version": "1.0",
    "author": "Eficent",
    "website": "www.eficent.com",
    "category": "Purchase Management",
    "depends": ["purchase_request_to_requisition",
                "purchase_request_operating_unit"],
    "description": """
Purchase Request to Call for Bids with Operating Units
======================================================
This module adds the possibility to create or update Requests for
Call for Bid from Purchase Request Lines.

Installation
============

No specific instructions required.


Configuration
=============

No specific instructions required.

Usage
=====
Go to the Purchase Request Lines from the menu entry 'Purchase Requests',
and also from the 'Purchase' menu.

Select the lines that you wish to initiate the RFQ for, then go to 'More'
and press 'Create Call for Bids'.

You can choose to select an existing Call for Bids or create a new one.

In case that you chose to select an existing Call for Bids,
the application will search for existing lines matching the request line,
and will add the extra quantity to them

In case that you create a new Call for Bids, the request lines will also be
consolidated into as few as possible lines in the RFQ.


For further information, please visit:

* https://www.odoo.com/forum/help-1


Known issues / Roadmap
======================

No issues have been identified


Credits
=======

Contributors
------------

* Jordi Ballester <jordi.ballester@eficent.com>


Maintainer
----------

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
    """,
    'installable': True,
    'active': False,
}
