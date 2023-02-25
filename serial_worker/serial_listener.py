from .serial_types import SensorSerial
import asyncio


class SensorListener:
    #  Sensor listener class. Listens to 
    def __init__(self, event: function, path: str, baud_rate: int = 9200, timeout=1) -> None:
        self.serial = SensorSerial(
            path=path,
            baud_rate=baud_rate,
            timeout=timeout
        )
        self.event = event
    
    async def start(self) -> None:
        while True:
            if (status:=self.serial.get_status()) != '':
                self.event(
                    time=int(status),
                    event_type=0
                )
            asyncio.sleep(1)
