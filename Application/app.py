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

<<<<<<< Updated upstream
<<<<<<< Updated upstream
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/places_db3.sqlite"
=======
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/places_db5.sqlite"
>>>>>>> Stashed changes
=======
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/places_db5.sqlite"
>>>>>>> Stashed changes
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
chinese = Base.classes.chinese
# Mexican = Base.classes.mexican
# Gyms = Base.classes.gyms
# Gas_stations = Base.classes.gas_stations
# Schools = Base.classes.schools

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


#     # Use Pandas to perform the sql query
#     stmt = db.session.query(Gyms).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[2:])

# @app.route("/gas_stations")
# def gas_stations():


#     # Use Pandas to perform the sql query
#     stmt = db.session.query(Gas_stations).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[2:])

# @app.route("/schools")
# def schools():
#     """Return a list of sample names."""

#     # Use Pandas to perform the sql query
#     stmt = db.session.query(Schools).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[2:])


# @app.route("/metadata/<sample>")
# def sample_metadata(sample):
#     """Return the MetaData for a given sample."""
#     sel = [
#         Samples_Metadata.City,
#         Samples_Metadata.Lat,
#         Samples_Metadata.Long,
#         Samples_Metadata.Name,
#         Samples_Metadata.Address,
#         Samples_Metadata.Rating,
        
#     ]

#     results = db.session.query(*sel).filter(Samples_Metadata.sample == sample).all()

#     # Create a dictionary entry for each row of metadata information
#     sample_metadata = {}
#     for result in results:
#         sample_metadata["sample"] = result[0]
#         sample_metadata["ETHNICITY"] = result[1]
#         sample_metadata["GENDER"] = result[2]
#         sample_metadata["AGE"] = result[3]
#         sample_metadata["LOCATION"] = result[4]
#         sample_metadata["BBTYPE"] = result[5]
#         sample_metadata["WFREQ"] = result[6]

#     print(sample_metadata)
#     return jsonify(sample_metadata)


# @app.route("/samples/<sample>")
# def samples(sample):
#     """Return `otu_ids`, `otu_labels`,and `sample_values`."""
#     stmt = db.session.query(Samples).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Filter the data based on the sample number and
#     # only keep rows with values above 1
#     sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]

#     # Sort by sample
#     sample_data.sort_values(by=sample, ascending=False, inplace=True)

#     # Format the data to send as json
#     data = {
#         "otu_ids": sample_data.otu_id.values.tolist(),
#         "sample_values": sample_data[sample].values.tolist(),
#         "otu_labels": sample_data.otu_label.tolist(),
#     }
#     return jsonify(data)


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
if __name__ == "__main__":
    app.run()