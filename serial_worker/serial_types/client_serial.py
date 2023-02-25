from .basic_serial import BasicSerial


class ClientSerial(BasicSerial):
    '''Class which handles all actions made to client'''

    def __init__(self, path: str, baud_rate: int = 9200, timeout=1) -> None:
        super().__init__(path, baud_rate, timeout)

    def set_state(self, left: int, right: int):
        '''
        Sets state of arrows on client
        '''
        self.write_serial(f"{left};{right}")
