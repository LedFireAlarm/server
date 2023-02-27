from serial_worker import ClientSerial, SensorListener
from config import SENSORS, CLIENTS
from models import Sensor
import asyncio
from storage import Event
from datetime import datetime, timedelta
from events import AlertEvents
import uuid
from typing import List


_loop = asyncio.new_event_loop()


async def test():
    while True:
        print("Async task ig")
        await asyncio.sleep(1)

async def comparation(client: ClientSerial):
    while True:
        print('asd')
        events: List[Event] = Event.select().where(Event.date > datetime.now() - timedelta(minutes=1))
        left_id = 1
        left_time: int = 0
        right_id = 0
        right_time: int = 0
        for event in events:
            if event.device_id == right_id:
                right_time += event.lenght
            elif event.device_id == left_id:
                left_time += event.lenght
        if (right_time + left_time) == 0:
            print("Zero")
            client.set_state(0,0)
        client.set_state(
            left_time / (left_time + right_time),
            right_time / (left_time + right_time)
        )


async def write_down_intersection(sensor: Sensor, time: int):
    print("Wrote ", time, " from ", sensor.hw_path)
    Event.create(
        uuid=uuid.uuid4(),
        device_id=sensor.id,
        date=datetime.now(),
        lenght=time,
        alert_type=AlertEvents.Alert.value
    )

clients_serial: List[ClientSerial] = []
for client in CLIENTS:
    clients_serial.append(ClientSerial(
        client.hw_path,
        client.baud_rate
    ))
for sensor in SENSORS:
    _loop.create_task(
        SensorListener(write_down_intersection, sensor).start()
    )
_loop.create_task(comparation(clients_serial[0]))

_loop.create_task(test())
# for client in CLIENTS:
#     await ClientSerial(client)
print(_loop.create_task())
_loop.run_forever()
