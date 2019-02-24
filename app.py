from flask import Flask, render_template, request, url_for
import json
import sys
from Query import retrieve_results
from FieldParser import parse_fields

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def homepage():
    json_result=[]

    if request.method == "POST":
        params = parse_fields(request.form)
        json_result = retrieve_results(params)
    
    return render_template('test.html', data=json_result)

if __name__ == '__main__':
    app.run()
