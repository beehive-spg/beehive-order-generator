from schematics.models import Model
from schematics.types import IntType, StringType

class Shop(Model):
    id = IntType(required=True, serialize_when_none=False, serialized_name='db/id')
    name = StringType(serialize_when_none=False, serialized_name='shop/name')