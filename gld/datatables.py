from clld.db.models import common
from clld.web.datatables.unit import Units
from clld.web.datatables.base import Col
from clld.db.meta import DBSession
from clldutils.misc import dict_merged

from gld.models import Word


class Words(Units):
    def __init__(self, req, model, **kw):
        Units.__init__(self, req, model, **kw)

    def base_query(self, query):
        return DBSession.query(common.Unit).filter(Word.language_pk == self.language.pk)

    def col_defs(self):
        res = [
            Col(
                self,
                'swadesh_id',
                sTitle='Swadesh ID',
                sDescription="Swadesh ID",
                model_col=Word.swadesh_id),
            Col(
                self,
                'swadesh_word',
                sTitle='Swadesh Word',
                sDescription="Swadesh Word",
                model_col=Word.swadesh_word),
            Col(
                self,
                'form',
                sTitle='Form',
                sDescription="Form",
                model_col=Word.form),
            Col(
                self,
                'cognation_index',
                sTitle='Cognation Index',
                sDescription="Cognation Index",
                model_col=Word.cognation_index),
            Col(
                self,
                'notes',
                sTitle='Notes',
                sDescription="Notes",
                model_col=Word.notes),
        ]
        return res

    def xhr_query(self):
        return dict_merged(super(Units, self).xhr_query())

    def get_options(self):
        return {'iDisplayLength': 20}


def includeme(config):
    config.register_datatable('units', Words)
