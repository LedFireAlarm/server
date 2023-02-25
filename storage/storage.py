from peewee import SqliteDatabase, Model
from peewee import CharField, DateTimeField, UUIDField, IntegerField
import uuid

db = SqliteDatabase("events.db3")


class BaseModel(Model):
    uuid = UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    class Meta:
        database = db


class Events(BaseModel):
    device_id = CharField()
    date = DateTimeField()
    lenght = IntegerField(null = True)
    alert_type = IntegerField(null=True)  # Lool in events.events.AlertEvents


db.connect()
db.create_tables([Events])
