from peewee import * 
db = SqliteDatabase("proyect1.db")


class User(Model):
    RFC = CharField(13)
    CURP = CharField(18)
    name = CharField()
    address = CharField(200)
    phone = IntegerField()
    email = CharField()
    password = CharField(100)

    class Meta:
        database = db