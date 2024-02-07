from peewee import SqliteDatabase, AutoField, CharField, DateField, ForeignKeyField, Model

db = SqliteDatabase('academia.db')

class Teachers(Model):
   teacher_id = AutoField()
   name = CharField()
   last_name = CharField()
   telephone = CharField()
   email = CharField(unique=True)

   class Meta:
       database = db

class Classes(Model):
   class_id = AutoField()
   code_class = CharField()
   start_date_course = DateField()
   end_date_course = DateField()
   schedule = CharField()
   teacher_id = ForeignKeyField(Teachers)

   class Meta:
       database = db

db.connect()
db.create_tables([Teachers, Classes])
