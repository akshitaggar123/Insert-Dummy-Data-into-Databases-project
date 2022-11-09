from app import db


class User(db.Model):
    __tablename__ = 'user_data'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    address = db.Column(db.String(200))

    def __init__(self, first_name: str, last_name: str, address: str):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def create(self):
        new_user = User(self.first_name, self.last_name, self.address)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def print_all_user():
        user_data = User.query.all()
        return user_data
