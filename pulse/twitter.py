from twython import Twython
from util import read_property
import requests


CONSUMER_KEY = read_property('consumer.key')
CONSUMER_SECRET = read_property('consumer.secret')
ACCESS_TOKEN = read_property('access.token')
ACCESS_TOKEN_SECRET = read_property('access.token.secret')
GEOCODING_KEY = read_property('geocoding.key')
GOOGLE_MAPS_API_URL = read_property('google.maps.api.url')


def search(hashtag, city, radius):
	t = Twython(app_key=CONSUMER_KEY, app_secret=CONSUMER_SECRET, oauth_token=ACCESS_TOKEN, oauth_token_secret=ACCESS_TOKEN_SECRET)
	params = {
		'address': city,
		'key': GEOCODING_KEY
	}
	req = requests.get(GOOGLE_MAPS_API_URL, params=params)
	res = req.json()
	result = res['results'][0]
	lat = result['geometry']['location']['lat']
	lng = result['geometry']['location']['lng']
	geocode = str(lat) + ',' + str(lng) + ',' + str(radius) + 'mi'
	print('geocode for ' + city + ' is ' + geocode)
	results = t.search(q=hashtag, geocode=geocode, lang='en', result_type='recent', count=10)
	tweets = results['statuses']
	return tweets