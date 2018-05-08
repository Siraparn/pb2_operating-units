# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockRequest(models.Model):

    _inherit = 'stock.request'

    operating_unit_id = fields.Many2one(
        'operating.unit',
        string='Operating Unit',
        default=lambda self: self.env['res.users'].
        operating_unit_default_get(self._uid),
    )
    # Borrow OU
    operating_unit_borrow_view_id = fields.Many2one(
        'operating.unit.view',
        string='Borrow from Operating Unit',
    )
    operating_unit_borrow_id = fields.Many2one(
        'operating.unit',
        compute='_compute_operating_unit_borrow_id',
        store=True,
    )
    # Borrow Location
    location_borrow_view_id = fields.Many2one(
        'stock.location.view',
        string='Borrow from Location',
        required=False,
        readonly=True,
        states={'draft': [('readonly', False)]},
        ondelete='restrict',
        domain="[('usage', '=', 'internal'),"
        "('for_stock_request', '=', True),"
        "('operating_unit_id', '=', operating_unit_borrow_id)]",
    )
    location_borrow_id = fields.Many2one(
        'stock.location',
        compute='_compute_location_borrow_id',
        readonly=True,
        store=True,
    )

    @api.onchange('operating_unit_borrow_view_id')
    def _onchange_operating_unit_borrow_view_id(self):
        self.location_borrow_view_id = False

    @api.one
    @api.depends('operating_unit_borrow_view_id')
    def _compute_operating_unit_borrow_id(self):
        self.operating_unit_borrow_id = self.operating_unit_borrow_view_id.id

    @api.one
    @api.depends('location_borrow_view_id')
    def _compute_location_borrow_id(self):
        self.location_borrow_id = self.location_borrow_view_id.id

    @api.model
    def _prepare_picking(self, request):
        res = super(StockRequest, self)._prepare_picking(request)
        res['operating_unit_id'] = request.operating_unit_id.id
        return res

    @api.onchange('operating_unit_id')
    def _onchange_operating_unit_id(self):
        ou_id = self.operating_unit_id.id
        types = self.env['stock.picking.type'].search(
            [('code', '=', 'internal'),
             ('warehouse_id.operating_unit_id', '=', ou_id),
             ('default_location_src_id.for_stock_request', '=', True)])
        # Only type with source location to be used for SR
        self.picking_type_id = types and types[0] or False
        res = {'domain': {'picking_type_id': [('id', 'in', (types.ids))]}}
        return res
