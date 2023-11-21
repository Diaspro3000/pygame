from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

@app.route("/")
def home():
    people_list = People.query.all()
    return render_template('index.html', people = people_list)

@app.route("/create/", methods  =['POST'])
def add():
    name = request.form.get('name')
    age = request.form.get('age')
    new_person = People(name=name, age=age)
    db.session.add(new_person)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:id>")
def delete(id):
    person = People.query.filter_by(id=id).first()
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True, port=5050)