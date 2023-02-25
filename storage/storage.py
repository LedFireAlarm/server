from peewee import SqliteDatabase, Model
from peewee import CharField, DateTimeField, UUIDField, IntegerField
import uuid

db = SqliteDatabase("events")


class BaseModel(Model):
    uuid = UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    class Meta:
        database = db


class Events(BaseModel):
    device_id = CharField()
    date = DateTimeField()
    alert_type = IntegerField()  # Lool in events.events.AlertEvents


db.connect()
db.create_tables([Events])
