from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from flask_debugtoolbar import DebugToolbarExtension

""" Connect Database. """
engine = create_engine("mysql+pymysql://root@localhost/Py2Db",echo=True)
db = scoped_session(sessionmaker(bind=engine))

""" Set html debugger. """
app = Flask(__name__)
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<replace with a secret key>'
toolbar = DebugToolbarExtension(app)

""" Display the flights list. """
@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("F_index.html",flights=flights)

""" Book a flight."""
@app.route("/book",methods=["POST"])
def book():
    #  Get form information.
    name = request.form.get("name")
    if not name:
        return render_template("F_error.html",message="Plz enter passenger name.")
    try:
        id = int(request.form.get("flight_id"))
    except:
        return render_template("F_error.html",message="Invalid flight id.")
    #  Make sure the flight exists.
    if db.execute("SELECT * FROM flights WHERE id=:id", {"id": id}).rowcount == 0:
        return render_template("F_error.html", message="No such flight with that id")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name,:flight_id)",{"name":name,"flight_id":id})
    db.commit()
    return render_template("F_Success.html")

""" See the flight detail. """
@app.route("/flights/<int:flight_id>")
def detail( flight_id ):
    #  Make sure flight exist
    flight = db.execute("SELECT * FROM flights WHERE id=:id", {"id": flight_id}).fetchone()
    if flight is None:
        return render_template("F_error.html", message="No such flight.")

        #  Get all passengers.
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()

    return render_template("F_flight.html", flight=flight, passengers=passengers)


