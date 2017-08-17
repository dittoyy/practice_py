from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict, dict_to_model
db = MySQLDatabase("dido1", host="127.0.0.1", port=3307, user="root", passwd="test")
db.connect()


class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)


if __name__ == "__main__":
    # User.create_table()#create
    # Tweet.create_table()


    # user = User.create(username='tom')#id
    # Tweet.create(user=user, message="this is 1 part wenzi")

    # user = User.create(username='tom1')
    # Tweet.create(user=user, message="this is 1 part wenzi1")
    # user = User.create(username='tom11')
    # Tweet.create(user=user, message="this is 1 part wenzi11")
    #
    Tweet.create(user_id=4, message="this is 2 part wenz333")#userid

    t = Tweet.get(message="this is 1 part wenzi11")#getonlyone
    print(t.user_id)
    print(t.created_date)
    print(t.is_published)

    ts = Tweet.filter(user_id=4)#filter
    for t in ts:
        print(t.message)

    # user = User.create(username='jack')
    # u = model_to_dict(user)#transfertodict{'username': 'jack', 'id': 5L}
    # print(u)

    user_data = {'id': 5, 'username': 'charlie'}
    user = dict_to_model(User, user_data)#transfertomodelobject{'username': 'jack', 'id': 5L}
    print(user.username)