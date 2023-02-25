from .basic_serial import BasicSerial


class SensorSerial(BasicSerial):
    '''Class which handles all the sensors job'''

    def __init__(self, path: str, baud_rate: int = 9200, timeout=1) -> None:
        super().__init__(path, baud_rate, timeout)

    def get_status(self):
        '''
        Gets status of sensors
        '''
        return self.read_serial()
        # self.write_serial(f"{left};{right}")
