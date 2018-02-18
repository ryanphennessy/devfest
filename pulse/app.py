from flask import Flask, render_template, request
from twitter import search
from sentiment import analyze


app = Flask(__name__)
app.config['DEBUG'] = True # Remove this


@app.route('/', methods=['POST', 'GET'])
def main_page():
	if request.method == 'POST':
		hashtag = '#' + request.form['user_search']
		city = request.form['city']
		radius = request.form['radius']
		tweets = search(hashtag, city, radius)
		if len(tweets) == 0:
			return render_template('no_results.html', city=city, topic=request.form['user_search'])
		tweets_text = []
		sentiments = []
		for tweet in tweets:
			print('Working on tweet ' + tweet['text'])
			tweets_text.append(tweet['text'])
			sentiments.append(analyze(tweet['text']))
		total_score = 0
		total_magnitude = 0
		for score, magnitude in sentiments:
			total_score += score
			total_magnitude += magnitude
		avg_score = total_score / len(sentiments)
		avg_magnitude = total_magnitude / len(sentiments)
		print('score ' + str(avg_score))
		sentiment = overall_sentiment(avg_score, avg_magnitude)
		return render_template('results.html', city=city, sentiment=sentiment, topic=request.form['user_search'], tweets=tweets_text)
	else:
		return render_template('search.html')

def overall_sentiment(avg_score, avg_magnitude):
	if avg_score < 0.1:
		return 'is not feeling so good about'
	elif avg_score < 0.2:
		return 'is feeling ok about'
	elif avg_score < 0.4:
		return 'is feeling pretty good about'
	else:
		return 'is feeling great about'


if __name__ == '__main__':
	app.run(host='0.0.0.0')