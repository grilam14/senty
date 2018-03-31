import feedparser
import requests
import re
from textblob import TextBlob
from bs4 import BeautifulSoup

'''
Allow for argument to be sent, screen for a valid stock, return unique score. 
'''


#Manually change the ticker to whatever stock acronym you want here
#GE is a terrible company in the news right now and gets a low score at around 6
#AAPL great company score above 10

ticker = 'GE'

site = "https://seekingalpha.com/api/sa/combined/.xml"


site = site[:41] + ticker + site[41:] 
'''This creates the xml site'''


d = feedparser.parse(site)

individualArticles = 'https://seekingalpha.com/symbol//news?source=feed_symbol_'
individualArticles = individualArticles[:32] + ticker + individualArticles[32:]
individualArticles = individualArticles[:61] + ticker + individualArticles[61:] 
'''this adds the ticker to two more places to check for the generic site filter '''

#print (individualArticles)

allarticles = ''
for entry in d.entries:

	if entry.link != individualArticles:
		url = entry.link
		response = requests.get(url);
		soup = BeautifulSoup(response.content, 'html.parser')
		line = ''

		for words in soup.findAll('p'):
			line += words.text.strip()

		allarticles+=line


#Textblob is the SA library I use to analyze the articles
sarticles = TextBlob(allarticles)
score = sarticles.sentiment.polarity
score = score*100

print(score)
	
		
