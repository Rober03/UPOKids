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

{
    "name": "UPOKids",
    "version": "1.0",
    "depends": ["base"],
    "author": "Roberto Juárez Bote\nCristian García Espino\nJosé Antonio Barrera Carmona",
    "category": "Education",
    "description": """
    Management UPOKids
    """,
    "init_xml": [],
    'data': ['activity_view.xml', 'upokidsclass_view.xml', 'student_view.xml', 'payment_view.xml',
             'instructor_view.xml', 'material_view.xml', 'installation_view.xml', 'owner_view.xml',
             'tournament_view.xml', 'externalschool_view.xml', 'student_workflow.xml'],
    'demo_xml': ['upokids_demo.xml'],
    'installable': True,
    'active': False,
}