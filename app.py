from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_info():
    return jsonify({
        "email": "bollodenis.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Bolodenis/hgn_internship_task0"
    })

if __name__ == "__main__":
    app.run(debug=True)
