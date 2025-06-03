from flask import Flask, request, render_template, make_response, redirect, url_for, Response, redirect, url_for, send_from_directory


app = Flask(__name__)

@app.route('/')
def home():
	title = "Home"
	return render_template("index.html", data=secrets.choice(quotes), title=title)

@app.route('/api')
def api(METHODS='get'):
	return secrets.choice(quotes)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('stare.html'), 404

@app.route('/humans.txt')
def humans():
	return Response("Made by Dan.", mimetype='text/plain')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=666, debug=True) # Remove debug mode when released
