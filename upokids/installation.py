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

class installation(osv.Model):
 
    _name = 'installation'
    _description = 'Insallation where to develop a UPOKids class'
 
    _columns = {
            'name':fields.char('Name', size=64, required=True, readonly=False),
            'address':fields.char('Address', size=64, required=True, readonly=False),
            'rentalprice':fields.integer('Rental Price'),
            'upokidsclass_ids': fields.one2many('upokidsclass','installation_id', 'Classes'),
            'owner_id': fields.many2one('owner','Owner', required=True),
            'tournamet_ids': fields.one2many('tournament','installation_id', 'Tournaments'),
    }

