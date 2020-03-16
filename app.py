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

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/happiness.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table

Freedom_short = Base.classes.freedom_idx_2019


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/freedom_columns")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Freedom_short).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


@app.route("/metadata/<iso_code>")
def sample_metadata(iso_code):
    """Return the MetaData for a given sample."""
    sel = [
        Freedom_short.iso_code,
        Freedom_short.year,
        Freedom_short.country,
        Freedom_short.region,
        Freedom_short.hf_score,
        Freedom_short.hf_rank,
        Freedom_short.hf_quartile,
    ]

    results = db.session.query(*sel).filter(Freedom_short.iso_code == iso_code).all()

    # Create a dictionary entry for each row of metadata information
    freedom_sdata_list = []
    for result in results:
        freedom_sdata = {}
        freedom_sdata["iso_code"] = result[0]
        freedom_sdata["year"] = result[1]
        freedom_sdata["country"] = result[2]
        freedom_sdata["region"] = result[3]
        freedom_sdata["hf_score"] = str(result[4])
        freedom_sdata["hf_rank"] = str(result[5])
        freedom_sdata["hf_quartile"] = result[6]
        freedom_sdata_list.append(freedom_sdata)    

    print(freedom_sdata_list)
    return jsonify(freedom_sdata_list)

if __name__ == "__main__":
    app.run()
