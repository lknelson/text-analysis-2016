import pandas

# Tells Jupyter to produce images in notebook
% pylab inline

# Makes images look good
style.use('ggplot')

# Read spreadsheet from the hard drive
dialogue_df = pandas.read_csv('antigone_dialogue.csv', index_col=0)

# Create a list of lists; split each character's dialogue into a list of tokens
dialogue_tokens = [character.split() for character in dialogue_df['DIALOGUE']]

# How many tokens are in each list?
dialogue_len = [len(tokens) for tokens in dialogue_tokens]

# Assign this as a new column in the dataframe
dialogue_df['WORDS_SPOKEN'] = dialogue_len

# Get the total number of words
total_words = sum(dialogue_df['WORDS_SPOKEN'])

# Use that total to normalize the share of words belonging to each character
# Multiply by 100 to convert to percentage
percent_by_character = dialogue_df['WORDS_SPOKEN'] / total_words * 100

# Add it as a new column to the dataframe
dialogue_df['WORDS_PCT'] = percent_by_character

# Re-sort in order of most prominent speaker
dialogue_df = dialogue_df.sort_values('WORDS_PCT',ascending=False)

# Visualize
dialogue_df['WORDS_PCT'].plot(kind='bar')
