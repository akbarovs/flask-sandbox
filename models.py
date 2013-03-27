from peewee import *
from app import db

class BaseModel(Model):
	class Meta:
		database = db

class Admin(BaseModel):
	first_name = CharField()
	last_name = CharField()
	fb_id = BigIntegerField(index=True)
	fb_group_id = BigIntegerField()
	email = CharField(null=True)
	fb_access_token = CharField(null=True)

class Group(BaseModel):
	name = CharField()
	description = TextField()
	email = CharField()
	fb_group_id = BigIntegerField()

	class Meta:
		db_table = 'fb_group'