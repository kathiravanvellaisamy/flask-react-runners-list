from flask import request,jsonify
from config import app,db
from models import Runner

@app.route("/runners",methods=["GET"])
def get_runners():
    runners = Runner.query.all()
    json_runners = list(map(lambda x: x.to_json(),runners))
    return jsonify({"runners": json_runners})

@app.route('/runners', methods=['GET', 'POST'])
def post_runners():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    phone = request.json.get("phone")
    category = request.json.get("category")
    blood_group = request.json.get("bloodGroup")
    tshirt_size = request.json.get("tshirtSize")

    if not first_name or not last_name or not email or not phone or not category or not blood_group or not tshirt_size:
        return (
            jsonify({"message":"All fields are required"}),
            400,
        )
    
    new_runner = Runner(first_name=first_name,last_name=last_name,email=email,phone=phone,category=category,blood_group=blood_group,tshirt_size=tshirt_size)
    try:
        db.session.add(new_runner)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}),400
    
    return jsonify({"message":"Runner created...!"}),201


if __name__ == "__main":
    with app.app_context():        
        db.create_all()
        app.run(debug=True)
