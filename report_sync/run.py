from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api
import Scheduler.scheduler as scheduler
import pandas as pd
import json

app = Flask(__name__)

if __name__ == '__main__':
    scheduler.scheduler.start()
    app.run(debug=False)
    