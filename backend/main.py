from flask import request,jsonify
from config import app,db
from models import Runner

@app.route("runners",methods=["GET"])
def get_runners():
    runners = Runner.query.all()
    json_runners = list(map(lambda x: x.to_json(),runners))
    return jsonify({"runners": json_runners})

if __name__ == "__main":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
