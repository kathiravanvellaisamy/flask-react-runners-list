from flask import request,jsonify
from config import app,db
from models import Runner

@app.route("/runners", methods=["GET"])
def get_runners():
    runners = Runner.query.all()
    json_runners = list(map(lambda x: x.to_json(),runners))
    return jsonify({"runners": json_runners})

@app.route("/create-runner",  methods=["POST"])
def post_runners():
    first_name = request.json.get("first_name")
    last_name = request.json.get("last_name")
    email = request.json.get("email")
    phone = request.json.get("phone")
    category = request.json.get("category")
    blood_group = request.json.get("blood_group")
    shirt_size = request.json.get("shirt_size")

    if not first_name or not last_name or not email or not phone or not category or not blood_group or not shirt_size:
        return jsonify({"message":"All fields are required"}),400
    
    
    new_runner = Runner(first_name=first_name,last_name=last_name,email=email,phone=phone,category=category,blood_group=blood_group,shirt_size=shirt_size)
    try:
        db.session.add(new_runner)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}),400
    
    return jsonify({"message":"Runner created...!"}),201


@app.route("/runners/<int:runner_id>",methods=["PATCH"])
def update_runner(runner_id):
    runner = Runner.query.get(runner_id)

    if not runner:
        return jsonify({"message":"User not found!"}), 404
    
    data = request.json
    runner.first_name = data.get("firstName",runner.first_name)
    runner.last_name = data.get("lastName",runner.last_name)
    runner.email = data.get("email",runner.email)
    runner.phone = data.get("phone",runner.phone)
    runner.category = data.get("category",runner.category)
    runner.blood_group = data.get("bloodGroup",runner.blood_group)
    runner.shirt_size = data.get("shirtSize",runner.shirt_size)

    db.session.commit()

    return jsonify({"message":"Runner details has been updated..."}), 200


@app.route("/delete_runner/<int:runner_id>",methods=["DELETE"])
def delete_runner(runner_id):
    runner = Runner.query.get(runner_id)

    if not runner:
        return jsonify({"message":"Runner not found..."}),404
    
    db.session.delete(runner)
    db.session.commit()

    return jsonify({"message":"Runner details has been deleted..."})

if __name__ == "__main":
    with app.app_context():        
        db.create_all()
        app.run(debug=True)
