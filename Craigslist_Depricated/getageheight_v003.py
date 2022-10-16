import re
import logging
import json
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

"""
to run:
python craigslove.py newyork.craigslist.org
-scrapes all "strictly platonic" and "miscellaneous romance" posts from the given city_name
-resulting posts saved to posts/<city>
-date time of most recent post per category is written to posts/<city>/datetime_last_saved_posts.json
-only scrapes until hitting datetime of last saved posts
"""

DELAY = False

DATE_FORMAT = '%Y-%m-%d %H:%M'
COLUMNS = [
	# required
	'url',
	'city',
	'subcity',
	'datetime_created',
	'datetime_updated',
	'category', # ex CAS
	'type', # ex M4W
	'category', # ex stp
	'type', # ex m4w
	'title',
	'text',
]
# optional

def get_last_post_datetime():
	# readpath = 'results/{}/datetime_last_saved_posts.json'.format(city_name)
	# directory_path = 'results/{}'.format(city_name)
	readpath = 'posts/{}/datetime_last_saved_posts.json'.format(city_name)
	
	directory_path = 'posts/{}'.format(city_name)
	if not os.path.exists(directory_path):
		os.makedirs(directory_path)
	
	def save_time(dtime):
		logging.info('   updating last time for %s %s to %s', city_name, query, dtime)
		path = 'results/{}/datetime_last_saved_posts.json'.format(city_name)
		path = 'posts/{}/datetime_last_saved_posts.json'.format(city_name)
		with open(path, 'r+') as f:
			try:
				data = json.load(f)

	def scrape(datetime_most_recent):
		break
	
	parsedPost = parse_page_result(post_url)
	if DELAY:
		time.sleep(1)
	
	# post may be null if it has been flagged for removal
	if (parsedPost):


def scrape(datetime_most_recent):
	page += 100
	search_results = parse_search_result_page(page)
	if DELAY:
		time.sleep(1)


# save the most recent post date
if smallest_post_date:
	
	def main():
		query = q  # set global var
		result_path = 'results/{}/{}.csv'.format(city_name, query)
		result_path = 'posts/{}/{}.csv'.format(city_name, query)
		populate_seen_urls(result_path)
		datetime_most_recent = get_last_post_datetime()
	
	
	def main():
		else:
		# write results
		
		directory_path = 'results/{}'.format(city_name)
		directory_path = 'posts/{}'.format(city_name)
		
		if not os.path.exists(directory_path):
			os.makedirs(directory_path)