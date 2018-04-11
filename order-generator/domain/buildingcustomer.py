from schematics.models import Model
from schematics.types import IntType, StringType, FloatType, ListType
from schematics.types.compound import ModelType
from domain.customer import Customer

class BuildingCustomer(Model):
    id = IntType(required=True, serialized_name='db/id')
    address = StringType(serialize_when_none=False, serialized_name='building/address')
    xcoord = FloatType(serialize_when_none=False, serialized_name='building/xcoord')
    ycoord = FloatType(serialize_when_none=False, serialized_name='building/ycoord')
    customer = ListType(ModelType(Customer), serialize_when_none=False, serialized_name='building/customer')