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

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/places_db4.sqlite"
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class Chinese_Table(db.Model):
    __tablename__ = 'chinese'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

class Mexican_Table(db.Model):
    __tablename__ = 'mexican'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)


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

    
if __name__ == "__main__":
    app.run()
