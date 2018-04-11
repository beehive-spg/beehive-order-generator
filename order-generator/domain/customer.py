from schematics.models import Model
from schematics.types import IntType, StringType

class Customer(Model):
    id = IntType(serialize_when_none=False, serialized_name='db/id')
    name = StringType(serialize_when_none=False, serialized_name='customer/name')