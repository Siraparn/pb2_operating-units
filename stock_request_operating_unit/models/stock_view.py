# -*- coding: utf-8 -*-
from openerp import models, fields


class StockLocationView(models.Model):
    _inherit = 'stock.location.view'

    for_stock_request = fields.Boolean(
        string='For Stock Request',
    )
