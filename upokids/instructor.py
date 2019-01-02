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

class instructor(osv.Model):
 
    _name = 'instructor'
    _description = 'UPOKid instructor'
 
    _columns = {
            'name':fields.char('Name', size=64, required=True, readonly=False),
            'subname':fields.char('Subname', size=64, required=True, readonly=False),
            'dni':fields.char('DNI', size=64, required=True, readonly=False),
            'phone1':fields.integer('Phone 1', required=True),
            'phone2':fields.integer('Phone 2', required=False),
            'email':fields.char('Email', size=64, required=False, readonly=False),
            'photo':fields.binary('Photo', required=False),
            'upokidsclass_ids': fields.one2many('upokidsclass','instructor_id', 'Classes'),
            'tournamet_ids': fields.one2many('tournament','instructor_id', 'Tournaments'), 
    }
    
    _sql_constraints = [     
                        ('dni_uniq', 'unique (dni)',
                         'The identification of the instructor must be unique'), ]
