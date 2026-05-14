from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Medico AI Backend Running"

@app.route("/api/doctors")
def doctors():
    return jsonify({
        "doctors": [
            "Dr. Sharma",
            "Dr. John",
            "Dr. David"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
