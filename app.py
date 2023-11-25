from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)


@app.post("/predict")
def predict():
  rext = request.get_json().get("message")
  # Rodo: check if text if valid
  response = get_response(rext)
  message = {"answer": response}
  return jsonify(message)

if __name__ == "__main__":
  app.run(debug=True)
