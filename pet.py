from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("proj 1(home).html")  # Homepage with pet listings
@app.route("/success")
def sucess():
    return render_template("success.html")
@app.route("/proj 1(adopt)")
def adopt_form():
    return render_template("proj 1(adopt).html")  # Adoption form page

@app.route("/submit", methods=["POST"])
def submit():
    
    data={
    "name":request.form.get("name"),
    "address":request.form.get("address"),
    "contact":request.form.get("contact"),
    "previous_pet":request.form.get("previous_pet"),
    "pet":request.form.get("pet"),
    "email":request.form.get("email"),
    "date":request.form.get("date"),
    "payment":request.form.get("payment"),
    "file":request.files.get("file").filename if request.files.get("file") else "No Files Uploaded"
    }
    return render_template("proj 1(thank).html",data=data)

if __name__ == "__main__":
    app.run(debug=True)