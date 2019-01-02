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

class upokidsclass(osv.Model):
 
    _name = 'upokidsclass'
    _description = 'Class scheduled in UPOKids'
 
    _columns = {
            'name':fields.char('Class name', size=64, required=True),
            'start': fields.datetime('Start', required=True, autodate=True),
            'end': fields.datetime('End', required=True, autodate=True),
            'capacity': fields.integer("Capacity"),
            'activity_id': fields.many2one('activity','Activity', required=True),
            'student_ids':fields.many2many('student', 'student_class_rel', 'class_id', 'student_id', 'Students'),
            'instructor_id': fields.many2one('instructor','Instructor'),
            'material_ids': fields.many2many( 'material','material_class_rel', 'class_id', 'material_id', 'Materials'),
            'installation_id':fields.many2one('installation','Installation'),
        } 