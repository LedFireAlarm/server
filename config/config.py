import json
from models import Client, Sensor, RelationMember

cfg = json.loads(
    open('configuration.json').read()
)

SENSORS = (
    Sensor(
        id=sensor['id'],
        is_real=sensor['is_real'],
        hw_path=sensor['hw_path'],
        baud_rate=sensor['baud_rate'],
        relatives=[
            RelationMember(
                id=relative['id'],
                side=relative['side']
            ) for relative in sensor['relatives']
        ]
    ) for sensor in cfg['sensors']
)
CLIENTS = (
    Client(
        id=client['id'],
        is_real=client['is_real'],
        hw_path=client['hw_path'],
        baud_rate=client['baud_rate'],
        relatives=[
            RelationMember(
                id=relative['id'],
                side=relative['side']
            ) for relative in client['relatives']
        ]
    ) for client in cfg['clients']
)
USE_PGDB = False
DEBUG = cfg['debug']
