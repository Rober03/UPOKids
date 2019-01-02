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

class payment(osv.Model):
 
    _name = 'payment'
    _description = 'payment made by a student'
 
    _columns = {
            'amount':fields.integer('Amount (Euros)', required=True),
            'date': fields.datetime('Date', required=True, autodate=True),
            'student_id': fields.many2one('student','Student', required=True),
            'activity_ids':fields.many2many('activity', 'payment_activity_rel', 'payment_id', 'activity_id', 'Activities', required=True),
    }
    
    def onchange_amount(self, cr, uid, ids, amount):
        a = amount
        if amount < 0:
            a = 0
        return {'value':{'amount':a}}
