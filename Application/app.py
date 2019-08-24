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

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/places_db5.sqlite"
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

class Gas_Stations_Table(db.Model):
    __tablename__ = 'gas_stations'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

class Gyms_Table(db.Model):
    __tablename__ = 'gyms'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

class Schools_Table(db.Model):
    __tablename__ = 'schools'
    __table_args__={'extend_existing':True}
    id = db.Column(db.Text, primary_key=True)

# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

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
    
if __name__ == "__main__":
    app.run()