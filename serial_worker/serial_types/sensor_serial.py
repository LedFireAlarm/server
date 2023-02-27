from .basic_serial import BasicSerial


class SensorSerial(BasicSerial):
    '''Class which handles all the sensors job'''

    def __init__(self, path: str, baud_rate: int = 9200, timeout=1) -> None:
        super().__init__(path, baud_rate, timeout)

    def get_status(self) -> int | None:
        '''
        Gets status of sensors
        '''
        time = self.read_serial()
        if time == '':
            return None
        if int(time) > 24:
            return time
        else:
            return None
        # self.write_serial(f"{left};{right}")
