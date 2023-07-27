from __future__ import annotations
import datetime
import uuid
from dacite.core import from_dict
import dacite
from typing import TypeVar, Type, Dict, List


T = TypeVar("T")

MAPPER_CONFIG = dacite.Config(
    cast = [
        uuid.UUID, 
    ],

    type_hooks = {
        datetime.datetime: datetime.datetime.fromisoformat,
        datetime.date: datetime.date.fromisoformat,
        datetime.time: datetime.time.fromisoformat,
    },
)


def map_dicts(data: List[Dict], class_type: Type[T]) -> List[T]:
    """Map the dictionaries to the specified type."""
    return [map_dict(d, class_type) for d in data]


def map_dict(data: Dict, class_type: Type[T]) -> T:
    """Map the given dictionary to the specified type"""
    return from_dict(class_type, data, MAPPER_CONFIG)


class IMappable:
    """Have a domain dataclass inherit this class to use ClassName.from_dict(data)."""
    
    @classmethod
    def from_dicts(cls, data: List[Dict]):
        return map_dicts(data, cls)

    @classmethod
    def from_dict(cls, data: Dict):
        return map_dict(data, cls)
    