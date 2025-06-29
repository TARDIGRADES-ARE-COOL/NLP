import nltk
# Download the tokenizer models if not already present
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re
import pandas as pd

# Functions for preprocessing

def remove_stopwords(data):
    """
    Remove stopwords from each review, mutating the word list in place.
    data: iterable of lowercase review strings
    returns: list of cleaned review strings (stopwords removed)
    """
    new = []
    for review in data:
        words = review.split()    # split the review into a list of words
        i = 0
        while i < len(words):
            if words[i] in en_stopwords:
                # remove the stopword and shift the rest down
                words.pop(i)
            else:
                # only advance index if we did not pop
                i += 1
        new.append(" ".join(words))  # re-join words into a cleaned string
    return new

def remove_punctuation(reviews):
    """
    Strip out all characters that are not word characters or whitespace.
    reviews: iterable of strings
    returns: list of cleaned strings without punctuation
    """
    cleaned = []
    # compile the regex once
    pattern = re.compile(r"([^\w\s])")

    for review in reviews:
        no_punct = pattern.sub("", review)  # remove punctuation
        cleaned.append(no_punct)

    return cleaned

def tokenize_reviews(reviews):
    """
    Split each review string into a list of word tokens.
    reviews: iterable of strings
    returns: list of token lists
    """
    tokenized = []
    for review in reviews:
        tokens = word_tokenize(review)  # NLTK word tokenizer
        tokenized.append(tokens)
    return tokenized

def lemmatization(data):
    """
    Lemmatize each token in each review.
    data: iterable of lists of tokens
    returns: list of lists of lemmatized tokens
    """
    lemmatizer = WordNetLemmatizer()
    new = []
    for token_list in data:
        lem = []
        for token in token_list:
            # perform lemmatization on each individual token
            lem.append(lemmatizer.lemmatize(token))
        new.append(lem)
    return new

# Load the data (make sure the CSV is in your script’s working folder)
data = pd.read_csv("tripadvisor_hotel_reviews.csv")

# 1. Lowercase the raw reviews
data["review_lowercase"] = data["Review"].str.lower()

# Prepare stopword list, but keep "not"
en_stopwords = stopwords.words("english")
en_stopwords.remove('not')

# 2. Remove stopwords
data["review_no_stopwords"] = remove_stopwords(data['review_lowercase'])

# 3. Remove punctuation (after stopword removal)
data['review_no_stopwords_no_punct'] = remove_punctuation(
    data["review_no_stopwords"]
)

# 4. Tokenize the cleaned reviews
data['tokenized'] = tokenize_reviews(
    data['review_no_stopwords_no_punct']
)

# 5. Lemmatize each token
data['lemmatized'] = lemmatization(data['tokenized'])

# Flatten all lemmatized tokens into a single list
tokens_clean = sum(data['lemmatized'], [])

# Compute unigram (1-gram) frequencies:
# 6a. Create 1-word tuples
one_word_tuples = nltk.ngrams(tokens_clean, 1)

# 6b. Build a pandas Series from the tuples
series_of_unigrams = pd.Series(one_word_tuples)

# 6c. Count how often each unique tuple (word) appears
unigrams = series_of_unigrams.value_counts()

# 7. Print the unigram counts
print(unigrams)
