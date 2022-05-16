from persist.persist import Database
from peewee import (
    Model, CharField, AutoField,
)

# model entity tbContatos


class TbContatos(Model):
    """Database Entity Class.

    Args:
        Model (peewee.Model): It is a database Model.
    """

    id = AutoField()
    name = CharField(max_length=80)
    email = CharField(max_length=120, null=True)
    mobile = CharField(max_length=20)
    tag = CharField(max_length=255, null=True)

    class Meta:
        # It calls database
        database = Database.open_it()
        # table name
        table_name = 'tbContatos'
