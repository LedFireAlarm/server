from . import RelationMember
from typing import List


class Sensor:
    def __init__(self, id: int, is_real: bool, hw_path: str, baud_rate: int, relatives: List[RelationMember] | None):
        self.id = id
        self.is_real = is_real
        self.hw_path = hw_path
        self.baud_rate = baud_rate
        self.relatives = relatives
