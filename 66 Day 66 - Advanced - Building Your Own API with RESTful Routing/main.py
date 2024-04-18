from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random as r

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    coffee_price = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def random():
    ## Tap into the existing db
    ## was able to do this by moving the cafes.db into the instance folder
    all_cafes = Cafe.query.all()
    ## Get a random record
    random_cafe = r.choice(all_cafes)
    ## Print out the fields
    print(random_cafe)
    print(random_cafe.name)
    return jsonify(cafe=random_cafe.to_dict())
    # return jsonify(can_take_calls=random_cafe.can_take_calls,
    #                coffee_price=random_cafe.coffee_price,
    #                has_sockets=random_cafe.has_sockets,
    #                has_toilet=random_cafe.has_toilet,
    #                has_wifi=random_cafe.has_wifi,
    #                id=random_cafe.id,
    #                img_url=random_cafe.img_url,
    #                location=random_cafe.location,
    #                map_url=random_cafe.map_url,
    #                name=random_cafe.name,
    #                seats=random_cafe.seats)


@app.route(rule="/all", methods=['GET'])
def all_records():
    cafes = []
    all_cafes = Cafe.query.all()
    print(all_cafes)
    for cafe in all_cafes:
        cafes.append(cafe.to_dict())
    all_records_dict = {"cafes": cafes}
    return jsonify(all_records_dict)


@app.route(rule="/search", methods=['GET'])
def search():
    loc = request.args.get('loc')
    print(loc)
    all_cafes_in_the_location = Cafe.query.filter_by(location=loc).all()
    if all_cafes_in_the_location:
        print(all_cafes_in_the_location)
        cafes_in_the_location = [cafe.to_dict() for cafe in all_cafes_in_the_location]
        cafes_in_the_location_dict = {"cafe": cafes_in_the_location}
        return jsonify(cafes_in_the_location_dict)
    else:
        error_dict = {"error": {"Not Found": "Sorry, we do not have a cafe at that location"}
                      }
        return jsonify(error_dict)


## HTTP POST - Create Record
@app.route(rule="/add", methods=['POST'])
def add():
    with app.app_context():
        print(type(bool(request.form['can_take_calls'])))
        new_cafe = Cafe(
            can_take_calls=bool(request.form['can_take_calls']),
            coffee_price=request.form['coffee_price'],
            has_sockets=bool(request.form['has_sockets']),
            has_toilet=bool(request.form['has_toilet']),
            has_wifi=bool(request.form['has_wifi']),
            img_url=request.form['img_url'],
            location=request.form['location'],
            map_url=request.form['map_url'],
            name=request.form['name'],
            seats=int(request.form['seats'])
        )
        db.session.add(new_cafe)
        db.session.commit()
    add_response = {"response": {"success": "Successfully added a new cafe"}}
    return jsonify(add_response)


## HTTP PUT/PATCH - Update Record
#PATCH
@app.route(rule="/update/<int:cafe_id>", methods=['PATCH'])
def update(cafe_id):
    with app.app_context():
        cafe_to_be_updated = Cafe.query.filter_by(id=cafe_id).first()
        # print(cafe_to_be_updated.name)
        new_price = request.args.get('coffee_price')
        if cafe_to_be_updated:
            cafe_to_be_updated.coffee_price = new_price
            db.session.commit()
            update_response = {"response": {"success": "Successfully updated the coffee_price"}}
            return jsonify(update_response), 200
        else:
            error_dict = {"error": {"Not Found": "Sorry, a cafe with that id was not found in the database"}
                      }
            return jsonify(error_dict), 404


## HTTP DELETE - Delete Record
@app.route(rule="/delete/<int:cafe_id>", methods=['DELETE'])
def delete(cafe_id):
    API_Key = request.args.get('api_key')
    if API_Key == "TopSecretAPIKey":
        # print('correct key')
        with app.app_context():
            cafe_to_be_deleted = Cafe.query.filter_by(id=cafe_id).first()
            # print(cafe_to_be_deleted)
            # print(cafe_to_be_deleted.name)
            if cafe_to_be_deleted:
                db.session.delete(cafe_to_be_deleted)
                db.session.commit()
                success = {
                    "Success": "Cafe Deleted"
                }
                return jsonify(success)
            else:
                no_cafe_found = {
                    "error": "Sorry, that cafe was not found in the database"
                }
                return jsonify(no_cafe_found)
    else:
        wrong_key = {
            "error": "Sorry, wrong API Key"
        }
        return jsonify(wrong_key)


if __name__ == '__main__':
    app.run(debug=True)

























# #PATCH
# @app.route(rule="/update/<int:cafe_id>", methods=['PATCH'])
# def update(cafe_id):
#     with app.app_context():
#         cafe_to_be_updated = Cafe.query.filter_by(id=cafe_id).first()
#         print(cafe_to_be_updated.name)
#         if cafe_to_be_updated:
#             parameter_to_be_updated = request.json["parameter"]
#             new_value = request.json["updated_value"]
#             print(parameter_to_be_updated)
#             print(new_value)
#             cafe_to_be_updated.parameter_to_be_updated = new_value
#             db.session.commit()
#             update_response = {"response": {"success": f"Successfully updated the {parameter_to_be_updated}"}}
#             return jsonify(update_response)
#         else:
#             error_dict = {"error": {"Not Found": "Sorry, a cafe with that id was not found in the database"}
#                       }
#             return jsonify(error_dict)






