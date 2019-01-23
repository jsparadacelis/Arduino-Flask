# Dependencies
from flask import Flask, request, jsonify, send_from_directory
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
import csv
import json


DOWNLOAD_DIRECTORY = "/home/neftali/Escritorio/pycontest/test/"

# Your API definition
app = Flask(__name__)
@app.route('/write_csv', methods=['POST'])
def write_csv():
    #obteniendo los valores del request
    json_ = request.get_json()
    file_name = "/home/neftali/Escritorio/pycontest/test/file.csv"
    with open(file_name, 'a') as csvfile:
        spamwriter = csv.writer(
            csvfile,
            delimiter=' ',
            quotechar=',', 
            quoting=csv.QUOTE_MINIMAL
        )
        spamwriter.writerow(json_["temp"])

    return "File"
    
@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    app.run(port=port, debug=True)