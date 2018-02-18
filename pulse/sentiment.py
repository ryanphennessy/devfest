import os
from util import read_property
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def analyze(tweet):
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = read_property('google.credentials.path')
	client = language.LanguageServiceClient()
	document = types.Document(content=tweet, type=enums.Document.Type.PLAIN_TEXT)
	sentiment = client.analyze_sentiment(document).document_sentiment
	return sentiment.score, sentiment.magnitude