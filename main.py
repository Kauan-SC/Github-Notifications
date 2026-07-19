from flask import Flask, request

app = Flask(__name__)

@app.route("/webhookcallback", methods=["POST"])
def hook():
    print(request.data)
    return "OK", 200

if __name__ == "__main__":
    app.run()