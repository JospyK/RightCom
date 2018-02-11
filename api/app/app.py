from flask import Flask, request, json, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET','POST'])

def index():
	records = []
	with open("logfile/Xlab.log", "r") as log_file:
		for raw_log_records in log_file:
			line = raw_log_records
			a, b, c = (line.split(','))
			a = a.replace('{"level":"','')
			a = a.replace('"','')
			b = b.replace('"message":"','')
			b = b.replace('"','')
			c = c.replace('"timestamp":"','')
			c = c.replace('"','')
			c = c.replace('}','')

			ligne = {}
			ligne["level"] = a
			ligne["message"] = b
			ligne["timestamp"] = c
			records.append(ligne)

	return jsonify(records)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response

app.run(debug=True)