import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/places_db4.sqlite"
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/places_db3.sqlite"
=======
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/places_db5.sqlite"
>>>>>>> Stashed changes
=======
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/places_db5.sqlite"
>>>>>>> Stashed changes
>>>>>>> kenny
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class Chinese_Table(db.Model):
    __tablename__ = 'chinese'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

<<<<<<< HEAD
class Mexican_Table(db.Model):
    __tablename__ = 'mexican'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)
=======
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

class Gas_Stations_Table(db.Model):
    __tablename__ = 'gas_stations'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

class Gyms_Table(db.Model):
    __tablename__ = 'gyms'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

<<<<<<< Updated upstream
=======
class Gas_Stations_Table(db.Model):
    __tablename__ = 'gas_stations'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

class Gyms_Table(db.Model):
    __tablename__ = 'gyms'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

>>>>>>> Stashed changes
class Schools_Table(db.Model):
    __tablename__ = 'schools'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

@app.route("/chinese")
def chinese():
    """Return a list of sample names."""

<<<<<<< Updated upstream
<<<<<<< Updated upstream
    # Use Pandas to perform the sql query
    stmt = db.session.query(chinese).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])

# initial chart showing the highest rated city by category

# @app.route("/mexican")
# def mexican():
   
#     # Use Pandas to perform the sql query
#     stmt = db.session.query(Mexican).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[2:])

# @app.route("/gyms")
# def gyms():
>>>>>>> kenny


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# Chinese_Table = Base.classes.chinese
# # mexican = Base.classes.mexican
# # gyms = Base.classes.gyms
# # gas_stations = Base.classes.gas_stations
# # schools = Base.classes.schools

@app.route("/")
def index():
    """Return the homepage."""

    Place1=Chinese_Table.query.filter_by(City='Overland Park').distinct()
    return render_template("index.html", counts=Place1)


# @app.route("/test")
# def test1():
#     """Return the homepage."""

#     Place2=Mexican_Table.query.filter_by(City='Overland Park').distinct()
#     return render_template("test.html", locations=Place2)


@app.route("/test2")
def test2():

    results = db.session.query(Chinese_Table.PlaceLatitude, Chinese_Table.PlaceLongitude ).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    latitude_mx = [result[0] for result in results]
    longitude_mx = [result[1] for result in results]

    # Generate the plot trace
    trace = {
        "lat": latitude_mx,
        "lng": longitude_mx
   
    }
    #  return render_template("test.html", locations=trace)
    return jsonify(trace)

@app.route("/test3")
def test3():

    results = db.session.query(Chinese_Table.PlaceRating, Chinese_Table.PlaceName, Chinese_Table.PlaceLatitude, Chinese_Table.PlaceLongitude ).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    rating1 = [result[0] for result in results]
    name1 = [result[1] for result in results]
    latitude_mx = [result[2] for result in results]
    longitude_mx = [result[3] for result in results]

    # Generate the plot trace
    trace2 = {
        "name" : name1,
        "lat": latitude_mx,
        "lng": longitude_mx,
        "rating": rating1
   
    }
    #  return render_template("test.html", locations=trace2)
    return jsonify(trace2)

<<<<<<< HEAD
    
=======
=======
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/chinese")
def chinese_results():

    results = db.session.query(Chinese_Table.PlaceRating, Chinese_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    rating = [result[0] for result in results]
    name = [result[1] for result in results]

    # Generate the plot trace
    trace = {
        "x" : name,
        "y": rating,
        "type": "bar"
    }
    #  return render_template("test.html", locations=trace2)
    return jsonify(trace)

@app.route("/mexican")
def mexican_results():

    results = db.session.query(Mexican_Table.PlaceRating, Mexican_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    rating2 = [result[0] for result in results]
    name2 = [result[1] for result in results]

    # Generate the plot trace
    trace2 = {
        "x" : name2,
        "y": rating2,
        "type": "bar"
    }
    #  return render_template("test.html", locations=trace)
    return jsonify(trace2)

@app.route("/gas_stations")
def gas_stations_results():

    results = db.session.query(Gas_Stations_Table.PlaceRating, Gas_Stations_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    rating3 = [result[0] for result in results]
    name3 = [result[1] for result in results]

    # Generate the plot trace
    trace3 = {
        "x" : name3,
        "y": rating3,
        "type": "bar"
    }
    #  return render_template("test.html", locations=trace2)
    return jsonify(trace3)

@app.route("/gyms")
def gyms_results():

    results = db.session.query(Gyms_Table.PlaceRating, Gyms_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    rating4 = [result[0] for result in results]
    name4 = [result[1] for result in results]

    # Generate the plot trace
    trace4 = {
        "x" : name4,
        "y": rating4,
        "type": "bar"
    }
    #  return render_template("test.html", locations=trace2)
    return jsonify(trace4)

@app.route("/schools")
def schools_results():

    results = db.session.query(Schools_Table.PlaceRating, Schools_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

=======
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/chinese")
def chinese_results():

    results = db.session.query(Chinese_Table.PlaceRating, Chinese_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    rating = [result[0] for result in results]
    name = [result[1] for result in results]

    # Generate the plot trace
    trace = {
        "x" : name,
        "y": rating,
        "type": "bar"
    }
    #  return render_template("test.html", locations=trace2)
    return jsonify(trace)

@app.route("/mexican")
def mexican_results():

    results = db.session.query(Mexican_Table.PlaceRating, Mexican_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    rating2 = [result[0] for result in results]
    name2 = [result[1] for result in results]

    # Generate the plot trace
    trace2 = {
        "x" : name2,
        "y": rating2,
        "type": "bar"
    }
    #  return render_template("test.html", locations=trace)
    return jsonify(trace2)

@app.route("/gas_stations")
def gas_stations_results():

    results = db.session.query(Gas_Stations_Table.PlaceRating, Gas_Stations_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    rating3 = [result[0] for result in results]
    name3 = [result[1] for result in results]

    # Generate the plot trace
    trace3 = {
        "x" : name3,
        "y": rating3,
        "type": "bar"
    }
    #  return render_template("test.html", locations=trace2)
    return jsonify(trace3)

@app.route("/gyms")
def gyms_results():

    results = db.session.query(Gyms_Table.PlaceRating, Gyms_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

    # Create lists from the query results
    rating4 = [result[0] for result in results]
    name4 = [result[1] for result in results]

    # Generate the plot trace
    trace4 = {
        "x" : name4,
        "y": rating4,
        "type": "bar"
    }
    #  return render_template("test.html", locations=trace2)
    return jsonify(trace4)

@app.route("/schools")
def schools_results():

    results = db.session.query(Schools_Table.PlaceRating, Schools_Table.PlaceName).\
        filter_by(City='Overland Park').distinct()

>>>>>>> Stashed changes
    # Create lists from the query results
    rating5 = [result[0] for result in results]
    name5 = [result[1] for result in results]

    # Generate the plot trace
    trace5 = {
        "x": name5,
        "y": rating5,
        "type": "bar"
    }
    #  return render_template("test.html", locations=trace2)
    return jsonify(trace5)
    
>>>>>>> Stashed changes
>>>>>>> kenny
if __name__ == "__main__":
    app.run()