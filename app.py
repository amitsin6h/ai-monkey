from flask import Flask, make_response
from flask import render_template, redirect, url_for, request
from flask import Response
from flask import jsonify
import random
import json
import plotly

import pandas as pd
import numpy as np

import quandl
import plotly.plotly as py
import plotly.tools as tls 
import plotly.graph_objs as go 

tls.set_credentials_file(username="amitsin6h", api_key="qF8b20oLOmNpxSML2cPs")

quandl.ApiConfig.api_key = '7Lf42wVbExJGFnUgisdM'




app = Flask(__name__)


client_data = {}


#app.route(rule, options)
@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')	




search_data = {}

@app.route('/search',methods = ['POST', 'GET'])
def result():
  if request.method == 'POST':
    search_data['search_query'] = request.form['search_query']
    return render_template("search.html", data = search_data)

  if request.method == 'GET':
    return render_template("search.html")







@app.route('/foo/<query>')
def foo(query):
	return 'you are searching for: ' + query







@app.route('/map')
def map():
    mydata = quandl.get("WIKI/AMZN", start_date="2014-12-31", end_date="2017-12-31")
    mydata = mydata.reset_index()


    graphs = [
        
        dict(
            data=[
                dict(
                    x=mydata.Date,  # Can use the pandas data structures directly
                    y=mydata['High']
                ),
                dict(
                    x=mydata.Date,  # Can use the pandas data structures directly
                    y=mydata['High']
                ),
                dict(
                    x=mydata.Date,  # Can use the pandas data structures directly
                    y=mydata['High']
                )
            ]
        )
    ]

    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('graph.html',
                           ids=ids,
                           graphJSON=graphJSON)













@app.route('/ai-monkey-search/<query>')
def ai_monkey_search(query):
	#print(query)
	#return 'you are searching for: ' + query
	if "stock market" in query:
		return render_template("about-stock-market.html", data = query)

	if "past" in query:
		amazone_share = quandl.get("WIKI/AMZN", start_date="2014-12-31", end_date="2017-12-31")
		amazone_share = amazone_share.reset_index()

		google_share = quandl.get("WIKI/GOOGL", start_date="2014-12-31", end_date="2017-12-31")
		google_share = google_share.reset_index()

		microsoft_share = quandl.get("WIKI/MSFT", start_date="2014-12-31", end_date="2017-12-31")
		microsoft_share = microsoft_share.reset_index()

		graphs = [
			dict(
				data=[
					dict(
						x=google_share.Date,  # Can use the pandas data structures directly
						y=google_share['Close'],
						name="GOOGL Close"
          ),
          dict(
						x=google_share.Date,  # Can use the pandas data structures directly
						y=google_share['Open'],
						name="GOOGL Open"
          )
          
				]
			),
			dict(
				data=[
					dict(
						x=amazone_share.Date,  # Can use the pandas data structures directly
						y=amazone_share['Close'],
						name="AMZN Close"
          ),
          dict(
						x=amazone_share.Date,  # Can use the pandas data structures directly
						y=amazone_share['Open'],
						name="AMZN Open"
          )
          
				]
			),
			dict(
				data=[
					dict(
						x=microsoft_share.Date,  # Can use the pandas data structures directly
						y=microsoft_share['Close'],
						name="MSFT Close"
          ),
          dict(
						x=microsoft_share.Date,  # Can use the pandas data structures directly
						y=microsoft_share['Open'],
						name="MSFT Open"
          )
          
				]
			),
			
    ]
    #ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
		ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
		graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

		return render_template("current-market-share.html", data = query, ids=ids,graphJSON=graphJSON)

	if "invest kare" in query:
		amazone_share = quandl.get("WIKI/AMZN", start_date="2014-12-31", end_date="2017-12-31")
		amazone_share = amazone_share.reset_index()
		graphs = [
			dict(
				data=[
					dict(
						x=amazone_share.Date,  # Can use the pandas data structures directly
						y=amazone_share['Close'],
						name="AMZN Close"
          ),
          dict(
						x=amazone_share.Date,  # Can use the pandas data structures directly
						y=amazone_share['Open'],
						name="AMZN Open"
          )
          
				]
			),
			
    ]
    #ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
		ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
		graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
		return render_template("invest-in-amazone.html", data = query, ids=ids, graphJSON=graphJSON)

	return 'you are searching for: ' + query












# @app.route('/login', methods=['POST','GET'])
# def login():
# 	if request.method == 'POST':
# 		username = request.form['nm']
# 		#hadoopState 
# 		return redirect(url_for('success/page', name=username))
# 	else:
# 		username = request.args.get('nm')
# 		return redirect(url_for('success/page', name=username))








if __name__ == '__main__':
	#app.run(host='0.0.0.0', port=5100, debug=True)
	app.run(port=5100, debug=True)
