######################################################################
# IMPORT FLASK AND OTHER DEFECIENCIS
######################################################################

import logging

from flask import current_app, Flask, redirect, render_template, url_for, request

from HealthCare.data import data_table, perperson_table
# from data import data_table, perperson_table
from HealthCare.health import problem_dd
# from health import problem_dd


def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)

    # Configure logging
    if not app.testing:
        logging.basicConfig(level=logging.INFO)


######################################################################
# HOME PAGE
######################################################################
    @app.route("/")
    def index():
        return render_template('indexB.html')

######################################################################
# DATA TABLE AND TABLEAU 
######################################################################
    @app.route("/data")
    def data():
    
        return render_template("data.html", data_index=data_table(), person_index=perperson_table())

######################################################################
# EAT YOUR WAY TO HEALTH - FOOD API
######################################################################

    @app.route("/health")
    def health():
        
        return render_template('health.html', problem_html=problem_dd())

    return app
