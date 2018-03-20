import datetime
import pandas as pd
import numpy as np
from collections import Counter
import os
import operator
import re
import nltk
import json
import random
import pickle
import json

from flask import Flask, url_for, redirect, request, jsonify, render_template, Response

app = Flask(__name__)

import platform
if platform.system() == 'Linux':
    path = ''
elif platform.system() == 'Darwin': 
    path = '/Users/am8e13/Dropbox/winepair/winepair/'

with open(path+'foodFlavorDictionaryForDinner.json') as infile: 
    foodFlavorDictionaryForDinner = json.load(infile)

with open(path+'wineFlavorDictionary.json') as infile: 
    wineFlavorDictionary = json.load(infile)

foods = set(foodFlavorDictionaryForDinner.keys())

@app.route('/', methods=['GET', 'POST'])
def index():
    error = ''
    if request.method == "POST":
        food = request.form['foodsearch']
        try:
            f = foodFlavorDictionaryForDinner[food]
            mind = 100
            minw = ''
            wine = None
            for w in wineFlavorDictionary.keys():
                mindtmp = np.sum((np.array(wineFlavorDictionary[w]) - np.array(f))**2)
                if (mind > mindtmp):
                    mind = mindtmp
                    wine = w
            return render_template('index.html', foods=foods, error=error, wine=wine)
        except:
            error = 'Your food is not in the database'
            return render_template('index.html', foods=foods, error=error)

    return render_template('index.html', foods=foods, error=error)