import mongoengine as db


database_name = 'dataox'
password = 'admin'
DB_URI = 'mongodb+srv://Vlad:{}@dataox.einirwf.mongodb.net/{}?retryWrites=true&w=majority'\
    .format(password, database_name)
db.connect(host=DB_URI)

class Room(db.Document):
    cost = db.StringField()
    image_url = db.StringField()
    date = db.StringField()


def save_info_in_db(cost, image_url, date):
    room = Room(
        cost=cost, 
        image_url=image_url, 
        date=date
        )
    room.save()
