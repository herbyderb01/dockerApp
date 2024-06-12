from flask import request, jsonify
from config import app, db
from models import Disc, Img
from werkzeug.utils import secure_filename


@app.route("/discs", methods=["GET"])
def get_discs():
    discs = disc.query.all()
    json_discs = list(map(lambda x: x.to_json(), discs))
    return jsonify({"discs": json_discs})


@app.route("/create_disc", methods=["POST"])
def create_disc():
    disc_brand = request.json.get("discBrand")
    disc_name = request.json.get("discName")
    flight_speed = request.json.get("discFlightSpeed")
    flight_glide = request.json.get("discFlightGlide")
    flight_turn = request.json.get("discFlightTurn")
    flight_fade = request.json.get("discFlightFade")
    disc_plastic = request.json.get("discPlastic")
    disc_weight = request.json.get("discWeight")
    disc_notes = request.json.get("discNotes")

    if not disc_name:
        return (
            jsonify({"message": "You must include a disc name."}),
            400,
        )

    new_disc = Disc(
        disc_brand=disc_brand,
        disc_name=disc_name,
        flight_speed=flight_speed,
        flight_glide=flight_glide,
        flight_turn=flight_turn,
        flight_fade=flight_fade,
        disc_plastic=disc_plastic,
        disc_weight=disc_weight,
        disc_notes=disc_notes
        )
    try:
        db.session.add(new_disc)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Disc created!"}), 201


@app.route("/update_disc/<int:disc_id>", methods=["PATCH"])
def update_disc(disc_id):
    disc = disc.query.get(disc_id)

    if not disc:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    disc.disc_brand = data.get("discBrand", disc.disc_brand)
    disc.disc_name = data.get("discName", disc.disc_name)
    disc.flight_speed = data.get("discFlightSpeed", disc.flight_speed)
    disc.flight_glide = data.get("discFlightGlide", disc.flight_glide)
    disc.flight_turn = data.get("discFlightTurn", disc.flight_turn)
    disc.flight_fade = data.get("discFlightFade", disc.flight_fade)
    disc.disc_plastic = data.get("discPlastic", disc.disc_plastic)
    disc.disc_weight = data.get("discWeight", disc.disc_weight)
    disc.disc_notes = data.get("discNotes", disc.disc_notes)

    db.session.commit()

    return jsonify({"message": "Disc updated."}), 200


@app.route("/delete_disc/<int:disc_id>", methods=["DELETE"])
def delete_disc(disc_id):
    disc = Disc.query.get(disc_id)

    if not disc:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(disc)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200


# @app.route('/upload', method=['POST'])
# def upload():
#     pic = request.files['pic']

#     if not pic:
#         return 'No pic uploaded', 400
    
#     filename = secure_filename(pic.filename)
#     mimetype = pic.mimetype
    
#     img = Img(img=pic.read(), mimetype=mimetype, name=filename)
#     db.session.add(img)
#     db.session.commit()

#     return 'Img has been uploaded', 200



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    with app.app_context():
        db.create_all()

    app.run(debug=True)