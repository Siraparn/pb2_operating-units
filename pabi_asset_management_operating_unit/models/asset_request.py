# -*- coding: utf-8 -*-
from openerp import models, fields, api


class AccountAssetRequest(models.Model):
    _inherit = 'account.asset.request'

    operating_unit_id = fields.Many2one(
        'operating.unit',
        string='Operating Unit',
        default=lambda self: self.env['res.users'].
        operating_unit_default_get(self._uid),
        required=True,
    )
