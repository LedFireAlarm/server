from .base_hw import BaseHW
from . import RelationMember
from typing import List


class Client(BaseHW):
    def __init__(self, id: int, is_real: bool, hw_path: str, baud_rate: int, relatives: List[RelationMember] | None):
        super().__init__(id, is_real, hw_path, baud_rate, relatives)
