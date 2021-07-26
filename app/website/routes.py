from website import app, db, bcrypt

@app.route("/home")
@app.route("/")
def home():
    return "hey there"