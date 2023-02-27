from peewee import SqliteDatabase, Model
from peewee import CharField, DateTimeField, UUIDField, IntegerField

db = SqliteDatabase("events.db.sqlite3")


class BaseModel(Model):
    uuid = UUIDField(primary_key=True, unique=True)

    class Meta:
        database = db


class Event(BaseModel):
    device_id = CharField()
    date = DateTimeField()
    lenght = IntegerField(null=True)
    alert_type = IntegerField(null=True)  # Look in events.events.AlertEvents


db.connect()
db.create_tables([Event])
