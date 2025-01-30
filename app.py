from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_info():
    return jsonify({
        "email": "bollodenis@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Bolodenis/hgn_task0"
    })

if __name__ == "__main__":
    app.run(debug=True)
