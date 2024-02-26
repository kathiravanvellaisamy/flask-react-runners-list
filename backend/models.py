from config import db

class Runner(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(80),unique=False,nullable=False)
    last_name = db.Column(db.String(80),unique=False,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    phone = db.Column(db.String(15),unique=False,nullable=False)
    category = db.Column(db.String(80),unique=False,nullable=False)
    blood_group = db.Column(db.String(80),unique=False,nullable=False)
    shirt_size = db.Column(db.String(80),unique=False,nullable=False)

    def to_json(self):
        return{
            "id":self.id,
            "first_name" :self.first_name,
            "last_name" : self.last_name,
            "email" : self.email,
            "phone" : self.phone,
            "category" : self.category,
            "blood_group" :self.blood_group,
            "shirt_size" : self.shirt_size
            
        }