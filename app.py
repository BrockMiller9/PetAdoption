from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)


@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        p = Pet(name=name, species=species,
                photo_url=photo_url, age=age, notes=notes)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route("/details/<int:pet_id>")
def show_details(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('details.html', pet=pet)


@app.route('/details/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    p = Pet.query.get(pet_id)
    form = AddPetForm(obj=p)
    if form.validate_on_submit():
        p.name = form.name.data
        p.species = form.species.data
        p.photo_url = form.photo_url.data
        p.age = form.age.data
        p.notes = form.notes.data

        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
