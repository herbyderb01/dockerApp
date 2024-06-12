from config import db


class Disk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disk_brand = db.Column(db.String(80), unique=False, nullable=True)
    disk_name = db.Column(db.String(80), unique=False, nullable=True)

    flight_speed = db.Column(db.Integer, unique=False, nullable=True)
    flight_glide = db.Column(db.Integer, unique=False, nullable=True)
    flight_turn = db.Column(db.Integer, unique=False, nullable=True)
    flight_fade = db.Column(db.Integer, unique=False, nullable=True)

    disk_plastic = db.Column(db.String(120), unique=False, nullable=True)
    disk_weight = db.Column(db.Integer, unique=False, nullable=True)
    disk_notes = db.Column(db.String(120), unique=False, nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "diskBrand": self.disk_brand,
            "diskName": self.disk_name,
            "diskFlightSpeed": self.flight_speed,
            "diskFlightGlide": self.flight_glide,
            "diskFlightTurn": self.flight_turn,
            "diskFlightFade": self.flight_fade,
            "diskPlastic": self.disk_plastic,
            "diskWeight": self.disk_weight,
            "diskNotes": self.disk_notes,
        }

class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)