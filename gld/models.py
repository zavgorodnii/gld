from zope.interface import implementer
from sqlalchemy import (
    Column,
    Unicode,
    Integer,
    ForeignKey,
)
from clld import interfaces
from clld.db.meta import CustomModelMixin
from clld.db.models.common import Unit


@implementer(interfaces.IUnit)
class Word(CustomModelMixin, Unit):
    pk = Column(Integer, ForeignKey('unit.pk'), primary_key=True)

    swadesh_id = Column(Integer)
    swadesh_word = Column(Integer)
    form = Column(Unicode)
    cognation_index = Column(Integer)
    notes = Column(Unicode)
