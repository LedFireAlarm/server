from serial_worker import ClientSerial, SensorListener
from config import SENSORS, CLIENTS
import asyncio


async def main():
    for sensor in SENSORS:
        SensorListener(
            
        )


asyncio.run(main(), debug=True)