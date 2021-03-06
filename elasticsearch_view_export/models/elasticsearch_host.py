# -*- coding: utf-8 -*-
#
#
#    Authors: Guewen Baconnier
#    Copyright 2015 Camptocamp SA
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
#

from elasticsearch import Elasticsearch

from openerp.osv import orm, fields


class ElasticsearchHost(orm.Model):
    _name = 'elasticsearch.host'
    _description = 'Elasticsearch Host'

    _rec_name = 'host'

    _columns = {
        'host': fields.char(string='Host', required=True),
    }

    def _es_client(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)):
            assert len(ids) == 1, "1 ID expected"
            ids = ids[0]
        host = self.browse(cr, uid, ids, context=context)
        return Elasticsearch([host.host])
