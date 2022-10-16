## Importing Libraries
import requests
import pandas as pd
import time
import random
import re
import numpy as np
import _pickle as pickle
from tqdm import tqdm_notebook as tqdm
from bs4 import BeautifulSoup as bs

## Using BeautifulSoup

# Randomizing the refresh rate
seq = [i / 10 for i in range(8, 18)]

# Creating a list of bios
biolist = []

# Gathering bios by looping and refreshing the web page
for _ in tqdm(range(1000)):
	
	# Refreshing the page
	page = requests.get("[insert website url here]")
	soup = bs(page.content)
	
	try:
		# Getting the bios
		bios = soup.find('div', class_='row no-margin for-sign').find_all('p')
		
		# Adding to a list of the bios
		biolist.extend([re.findall('"([^"]*)"', i.text) for i in bios])
	except:
		pass
	
	# Sleeping
	time.sleep(random.choice(seq))

# Creating a DF from the bio list
bio_df = pd.DataFrame(biolist, columns=['Bios'])