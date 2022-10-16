# List of potential Dating questions/categories
qs = ['Movies',
      'TV',
      'Religion',
      'Music',
      'Sports',
      'Books',
      'Politics']

# Creating a DF of the questions/categories
topic_df = pd.DataFrame(columns=qs)

# Filling in Data
for i in topic_df.columns:
	
	# Range of numbers to represent different labels in each category
	topic_df[i] = np.random.randint(0, 10, bio_df.shape[0])

# Logic: The numbers represent a specific choice within the categories
# So your number 1 preferred artist/song/album under the Music, your one favorite movie, etc.

# Joining the two dataframes
final_df = bio_df.join(topic_df)
final_df

# Exporting the complete DF
with open("profiles.pkl", "wb") as fp:
	pickle.dump(final_df, fp)