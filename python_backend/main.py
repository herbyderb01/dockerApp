from flask import request, jsonify
from config import app, db
from models import Disk, Img
from werkzeug.utils import secure_filename


@app.route("/disks", methods=["GET"])
def get_disks():
    disks = Disk.query.all()
    json_disks = list(map(lambda x: x.to_json(), disks))
    return jsonify({"disks": json_disks})


@app.route("/create_disk", methods=["POST"])
def create_disk():
    disk_brand = request.json.get("diskBrand")
    disk_name = request.json.get("diskName")
    flight_speed = request.json.get("diskFlightSpeed")
    flight_glide = request.json.get("diskFlightGlide")
    flight_turn = request.json.get("diskFlightTurn")
    flight_fade = request.json.get("diskFlightFade")
    disk_plastic = request.json.get("diskPlastic")
    disk_weight = request.json.get("diskWeight")
    disk_notes = request.json.get("diskNotes")

    if not disk_name:
        return (
            jsonify({"message": "You must include a disk name."}),
            400,
        )

    new_disk = Disk(
        disk_brand=disk_brand,
        disk_name=disk_name,
        flight_speed=flight_speed,
        flight_glide=flight_glide,
        flight_turn=flight_turn,
        flight_fade=flight_fade,
        disk_plastic=disk_plastic,
        disk_weight=disk_weight,
        disk_notes=disk_notes
        )
    try:
        db.session.add(new_disk)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Disk created!"}), 201


@app.route("/update_disk/<int:user_id>", methods=["PATCH"])
def update_disk(user_id):
    disk = disk.query.get(user_id)

    if not disk:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "Usr updated."}), 200


@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)
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