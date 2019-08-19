import pandas as pd
import datetime as dt

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[enter_start_date]<br/>"
        f"/api/v1.0/[enter_start_date]/[enter_end_date]"
    )
    
@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all dates and prcps
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    all_prcps = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[f"{date}"] = prcp
        all_prcps.append(prcp_dict)

    return jsonify(all_prcps)

@app.route("/api/v1.0/stations")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station, Station.name).all()

    session.close()

    all_stations = []
    for station, name in results:
        station_dict = {}
        station_dict[f"{station}"] = f"{name}"
        all_stations.append(station_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    qry = session.query(func.max(Measurement.date))[0]
    max_date = pd.to_datetime(qry)
    d = max_date - dt.timedelta(days=365)
    date = d.strftime("%Y-%m-%d")[0]
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date)


    session.close()

    past_year_tobs = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[f"{date}"] = prcp
        past_year_tobs.append(prcp_dict)

    return jsonify(past_year_tobs)


@app.route(f"/api/v1.0/<start_date>")
def calc_temps(start_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    session.close()

    calc_temps = []
    for min, avg, max in results:
        tmp_dict = {}
        tmp_dict["Min"] = min
        tmp_dict["Avg"] = avg
        tmp_dict["Max"] = max
        calc_temps.append(tmp_dict)

    return jsonify(calc_temps)

@app.route(f"/api/v1.0/<start_date>/<end_date>")
def calc_temps_end(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    calc_temps = []
    for min, avg, max in results:
        tmp_dict = {}
        tmp_dict["Min"] = min
        tmp_dict["Avg"] = avg
        tmp_dict["Max"] = max
        calc_temps.append(tmp_dict)

    return jsonify(calc_temps)
    
if __name__ == '__main__':
     app.run(debug=True)