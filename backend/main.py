from flask import Flask,jsonify
import database as DB
from API_router import api

app = Flask(__name__)
app.register_blueprint(api)
app.config["JSON_SORT_KEYS"] = False

@app.route("/")
def index():
    print("index")
    return jsonify({
        "result":True,
        "data":"index_page"
    })
    
if __name__ == "__main__":
    DB.create_database()
    session = DB.create_session()
    app.run(host="0.0.0.0",debug=True,post=8080)
