from flask import Flask, jsonify

from datetime import datetime, timezone
import requests

app = Flask(__name__)


@app.route("/me", methods=["GET"])
def get_profile():
    try:
        # Fetch random cat fact with timeout
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()  # Raise error for bad responses (4xx/5xx)
        data = response.json()
        cat_fact = data.get("fact", "No cat fact available at the moment.")
    except requests.RequestException:
        # Handle any network/API errors gracefully
        cat_fact = "Could not fetch a cat fact at the moment. Please try again later."

    # Prepare the response in the required format
    result = {
        "status": "success",
        "user": {
            "email": "bollodenis@gmail.com",
            "name": "Denis Bollo",
            "stack": "Python/Flask"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),  # Current UTC time in ISO 8601
        "fact": cat_fact
    }

    return jsonify(result), 200  # Return JSON with HTTP 200 OK

if __name__ == "__main__":
    app.run()




