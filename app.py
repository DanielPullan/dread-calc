from flask import Flask, request, render_template, make_response, redirect, url_for, Response, redirect, url_for, send_from_directory


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
	title = "Home"
	data = "Data"

# DREAD is a risk assessment model. It's made up of 5 components:
# - Damage: How much damage could an attack cause.
# - Reproducibility: How easily can the same attack be repeated.
# - Exploitability: How difficult is it to actually launch an attack.
# - Affected Users: How many assets are affected by the attack.
# - Discoverability: How easily can the vulnerability be discovered.

	if request.method == 'POST':
		form_damage = int(request.form['damage'])
		form_reproducibility = int(request.form['reproducibility'])
		form_exploitability = int(request.form['exploitability'])
		form_affectedUsers = int(request.form['affectedUsers'])
		form_discoverability = int(10) # Always treated as 10

		print(form_damage)
		print(form_reproducibility)
		print(form_exploitability)
		print(form_affectedUsers)
		print(form_discoverability)

		dread_score = int((form_damage + form_reproducibility + form_exploitability + form_affectedUsers
			+ form_discoverability) / 5)

		print(dread_score)

		return render_template("result.html", title=title, data=data, dread_score=dread_score)

	return render_template("index.html", title=title, data=data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('stare.html'), 404

@app.route('/humans.txt')
def humans():
	return Response("Made by Dan.", mimetype='text/plain')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=666, debug=True) # Remove debug mode when released
