# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Eficent (<http://www.eficent.com/>)
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
from openerp import models, api, _


class Procurement(models.Model):
    _inherit = 'procurement.order'

    @api.model
    def create_procurement_purchase_order(self, procurement,
                                          po_vals, line_vals):
        if procurement.location_id:
            po_vals.update({'operating_unit_id':
                            procurement.location_id.operating_unit_id.id})
        return super(Procurement, self).\
            create_procurement_purchase_order(procurement, po_vals, line_vals)

    @api.model
    def _prepare_purchase_request(self, procurement):
        res = super(Procurement, self)._prepare_purchase_request(procurement)
        if procurement.location_id.operating_unit_id:
            res.update({
                'operating_unit_id':
                    procurement.location_id.operating_unit_id.id
            })
        return res

    @api.one
    @api.constrains('location_id', 'request_id')
    def _check_purchase_request_operating_unit(self):
        if self.request_id and self.location_id.operating_unit_id and \
                        self.request_id.operating_unit_id != \
                        self.location_id.operating_unit_id:
            raise Warning(_('The Purchase Request and the Procurement Order '
                            'must belong to the same Operating Unit.'))

    @api.one
    @api.constrains('location_id', 'warehouse_id')
    def _check_warehouse_operating_unit(self):
        if self.warehouse_id and self.location_id.operating_unit_id and \
                        self.warehouse_id.operating_unit_id != \
                        self.location_id.operating_unit_id:
            raise Warning(_('Warehouse and location of procurement order '
                            'must belong to the same Operating Unit.'))
