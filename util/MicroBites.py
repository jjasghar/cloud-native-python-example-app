import os
from flask import Flask, Response, jsonify, abort
from flask_restplus import Api, Resource, fields, reqparse
from flask_cors import CORS, cross_origin
import json
import pandas as pd
from dotenv import load_dotenv
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import logging
import sqlalchemy
import sys
from flask import request
from werkzeug.exceptions import HTTPException

# get logging level from the environment, default to INFO
logging.basicConfig(level=os.environ.get("LOGLEVEL", logging.INFO))

# Get a logger and keep its name in sync with this filename
logger = logging.getLogger(os.path.basename(__file__))

# load environment variables
load_dotenv()

# The application
app = Flask(__name__)
CORS(app)

logger.info('starting application')

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default to 8080
port = int(os.getenv('PORT', 8080))

# DB Connections and identifier constants
SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://"+ os.getenv('MARIADB_USERNAME')
                            +":"+ os.getenv("MARIADB_PASSWORD")
                            +"@"+ os.getenv("MARIADB_HOST")
                            +":" + str(os.getenv("MARIADB_HOST"))
                            +"/prometeo")

DB_ENGINE = sqlalchemy.MetaData(SQLALCHEMY_DATABASE_URI).bind
ANALYTICS_TABLE = 'meal_status_analytics'
meal_ID_COL = 'meal_id'
TIMESTAMP_COL = 'timestamp_mins'
STATUS_LED_COL = 'analytics_status_LED'

# We initialize the prometeo Analytics engine.
# Calculates Time-Weighted Average exposures and exposure-limit status 'gauges' for all meals for the last minute.
def callCreateMenu():
    logger.info('Running analytics')

    # Start up a scheduled job to run once per minute
    ANALYTICS_FREQUENCY_SECONDS = 60
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=callMicrobitesAnalytics, trigger="interval", seconds=ANALYTICS_FREQUENCY_SECONDS)
    scheduler.start()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

