from flask import Flask, request, render_template, make_response, Response, redirect, url_for, send_from_directory, flash
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('secret_key')

if not app.secret_key:
    raise RuntimeError("Secret key not loaded.")

@app.route('/', methods=['POST', 'GET'])
def home():
	dread_values = {'damage': '', 'reproducibility': '', 'exploitability': '',
        'affectedUsers': '', 'discoverability': 10
	}
	dread_score = None

	if request.method == 'POST':
		try:
			form_damage = 			int(request.form.get('damage', ''))
			form_reproducibility = 	int(request.form.get('reproducibility', ''))
			form_exploitability = 	int(request.form.get('exploitability', ''))
			form_affectedUsers = 	int(request.form.get('affectedUsers', ''))
			form_discoverability = 	10 # Always treated as 10 for calculation

			dread_values = {
	                'damage': 			form_damage, 
	                'reproducibility': 	form_reproducibility,
	                'exploitability': 	form_exploitability, 
	                'affectedUsers': 	form_affectedUsers,
	                'discoverability': 	10
	            }

			if not (1 <= form_damage 			<= 10 and
					1 <= form_reproducibility 	<= 10 and
					1 <= form_exploitability 	<= 10 and
					1 <= form_affectedUsers 	<= 10):
				flash('All DREAD component scores must be integers between 1 and 10.', 'error')
				return render_template("index.html", **dread_values)

			dread_score = int((	form_damage + 
								form_reproducibility + 
								form_exploitability + 
								form_affectedUsers + 
								form_discoverability) 
								/ 5)

			return render_template("result.html", **dread_values, dread_score=dread_score)

		except ValueError:
			flash('Please ensure all DREAD component scores are valid numbers.', 'error')
			return render_template("index.html", **dread_values)
		
		except Exception as e:
			flash(f'An unexpected error occurred: {e}', 'error')
			print(f"Error: {e}")
			return render_template("index.html", **dread_values)
		
	return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('stare.html'), 404

@app.route('/humans.txt')
def humans():
	return Response("Made by Dan.", mimetype='text/plain')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=666, debug=True) # Remove debug mode when released
