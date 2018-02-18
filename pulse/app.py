from flask import Flask, render_template, request
from twitter import search


app = Flask(__name__)
app.config['DEBUG'] = True # Remove this


@app.route('/', methods=['POST', 'GET'])
def main_page():
	if request.method == 'POST':
		hashtag = '#' + request.form['user_search']
		city = request.form['city']
		radius = request.form['radius']
		tweets = search(hashtag, city, radius)
		tweets_text = []
		for tweet in tweets:
			tweets_text.append(tweet['text'])
		return render_template('results.html', tweets=tweets_text)
	else:
		return render_template('search.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0')