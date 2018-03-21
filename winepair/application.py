import numpy as np
import json
import re

from flask import Flask, url_for, redirect, request, jsonify, render_template, Response

application = Flask(__name__)

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

@application.route('/', methods=['GET', 'POST'])
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

                def splitwine(w):
                    s = re.split("([A-Z][^A-Z]*)", w)[1:-1]
                    if len(s)>1:
                        return s[0] + ' ' + s[2]
                    else:
                        return s[0]

                wine = splitwine(wine)

            return render_template('index.html', foods=foods, error=error, wine=wine)
        except:
            error = 'Your food is not in the database'
            return render_template('index.html', foods=foods, error=error)

    return render_template('index.html', foods=foods, error=error)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()