# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class material(osv.Model):
 
    _name = 'material'
    _description = 'UPOKid material'
 
    _columns = {
            'name':fields.char('Name', size=64, required=True, readonly=False),
            'units':fields.integer('Units', required=True),
            'description':fields.text('Description', required=False),
            'photo':fields.binary('Photo', required=False),
            'upokidsclass_ids':fields.many2many('upokidsclass', 'material_class_rel', 'material_id', 'class_id', 'Classes'),
            'tournament_ids':fields.many2many('tournament', 'tournament_material_rel', 'material_id', 'tournament_id', 'Tournaments'), 
    }
    def _check_stock(self, cr, uid, ids): 
        return self.browse(cr, uid, ids)[0].units >= 0
    
    _constraints = [(_check_stock, 'Wrong Stock', ['units']), ] 
