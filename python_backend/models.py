from config import db


class Disc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disc_brand = db.Column(db.String(80), unique=False, nullable=True)
    disc_name = db.Column(db.String(80), unique=False, nullable=True)

    flight_speed = db.Column(db.Integer, unique=False, nullable=True)
    flight_glide = db.Column(db.Integer, unique=False, nullable=True)
    flight_turn = db.Column(db.Integer, unique=False, nullable=True)
    flight_fade = db.Column(db.Integer, unique=False, nullable=True)

    disc_plastic = db.Column(db.String(120), unique=False, nullable=True)
    disc_weight = db.Column(db.Integer, unique=False, nullable=True)
    disc_notes = db.Column(db.String(120), unique=False, nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "discBrand": self.disc_brand,
            "discName": self.disc_name,
            "discFlightSpeed": self.flight_speed,
            "discFlightGlide": self.flight_glide,
            "discFlightTurn": self.flight_turn,
            "discFlightFade": self.flight_fade,
            "discPlastic": self.disc_plastic,
            "discWeight": self.disc_weight,
            "discNotes": self.disc_notes,
        }

class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)