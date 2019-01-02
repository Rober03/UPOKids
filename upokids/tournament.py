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

class tournament(osv.Model):
 
    _name = 'tournament'
    _description = 'tournament managed by a instructor'
    
    def _schools(self, cr, uid, ids, name, args, context=None):
        res = {}
        for tournament in self.browse(cr, uid, ids):
            res[tournament.id] = len(tournament.externalschool_ids)
        return res
    
    def removeMaterial(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'material_ids':[(5,)]}, context=None)  
 
    _columns = {
            'name':fields.char('Name', size=64, required=True, readonly=False),
            'instructor_id': fields.many2one('instructor','Instructor'),
            'start': fields.datetime('Start', required=True, autodate=True),
            'end': fields.datetime('End', required=True, autodate=True),
            'material_ids':fields.many2many('material', 'tournament_material_rel', 'tournament_id', 'material_id', 'Materials'), 
            'installation_id': fields.many2one('installation','Installation'),
            'externalschool_ids':fields.many2many('externalschool', 'externalschool_tournament_rel', 'tournament_id', 'externalschool_id', 'External Schools'),
            'number_school':fields.function(_schools, type="integer", string="Number of Schools", store=True),
    }
