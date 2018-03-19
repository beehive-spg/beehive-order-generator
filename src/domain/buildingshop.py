from schematics.models import Model
from schematics.types import IntType, StringType, FloatType, ListType
from schematics.types.compound import ModelType
from domain.shop import Shop

class BuildingShop(Model):
    id = IntType(required=True, serialized_name='db/id')
    address = StringType(serialize_when_none=False, serialized_name='building/address')
    xcoord = FloatType(serialize_when_none=False, serialized_name='building/xcoord')
    ycoord = FloatType(serialize_when_none=False, serialized_name='building/ycoord')
    shop = ListType(ModelType(Shop), serialize_when_none=False, serialized_name='building/shop')