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

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
chinese = Base.classes.chinese
mexican = Base.classes.mexican
gyms = Base.classes.gyms
gas_stations = Base.classes.gas_stations
schools = Base.classes.schools

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/chinese")
def chinese():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(chinese).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])

# initial chart showing the highest rated city by category

@app.route("/mexican")
def mexican():
   
#     # Use Pandas to perform the sql query
    stmt = db.session.query(Mexican).statement
    df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])

@app.route("/gyms")
def gyms():


#     # Use Pandas to perform the sql query
    stmt = db.session.query(Gyms).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[2:])

@app.route("/gas_stations")
def gas_stations():


#     # Use Pandas to perform the sql query
    stmt = db.session.query(Gas_stations).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])

@app.route("/schools")
def schools():
#     """Return a list of sample names."""

#     # Use Pandas to perform the sql query
    stmt = db.session.query(Schools).statement
    df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


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


if __name__ == "__main__":
    app.run()
