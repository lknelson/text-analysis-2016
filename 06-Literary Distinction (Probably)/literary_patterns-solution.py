import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Assign file paths to each set of poems
review_path = 'poems/reviewed/'
random_path = 'poems/random/'

# Get lists of text files in each directory
review_files = os.listdir(review_path)
random_files = os.listdir(random_path)

# Read in texts as strings from each location
review_texts = [open(review_path+file_name).read() for file_name in review_files]
random_texts = [open(random_path+file_name).read() for file_name in random_files]

# Collect all texts in single list
all_texts = review_texts + random_texts

# Get all file names together
all_file_names = review_files + random_files

# Keep track of classes with labels
all_labels = ['reviewed'] * len(review_texts) + ['random'] * len(random_texts)

# Intitialize the function that will transform our list of texts to a DTM
cv = CountVectorizer(stop_words = 'english', min_df=180, binary = True, max_features = None)

# Transform our texts to DTM
dtm = cv.fit_transform(all_texts).toarray()

# Train the classifier and assign it to a variable
nb = MultinomialNB()
nb.fit(dtm, all_labels)

# Canonic file path
canonic_path = 'poems/canonic/'

# Get list of file names in canonic directory
canonic_files = os.listdir(canonic_path)

# Read in canonic texts
canonic_texts = [open(canonic_path+file_name).read() for file_name in canonic_files]

# Transform into DTM
canonic_dtm = cv.transform(canonic_texts)

# Make predictions
nb.predict(canonic_dtm)
