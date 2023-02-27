from .serial_types import SensorSerial
from models import Sensor
import asyncio


class SensorListener:
    '''
    Класс прослушавания ивентов с датчиков.
    '''
    def __init__(
            self,
            event: asyncio.coroutines,
            sensor: Sensor,
            timeout: int = 1
    ) -> None:
        if sensor.is_real:
            self.serial = SensorSerial(
                path=sensor.hw_path,
                baud_rate=sensor.baud_rate,
                timeout=timeout
            )
        print(sensor.hw_path)
        self.event = event
        self.sensor = sensor

    async def start(self) -> None:
        '''
        Начинает слушать о новых проишествиях.
        При наличии таковых оповещения вызывает функцию
        '''
        while True:
            if (status := self.serial.get_status()):
                await self.event(
                    sensor=self.sensor,
                    time=int(status)
                )
