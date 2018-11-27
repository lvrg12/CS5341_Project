import os
import math
import csv
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

def main():

    # Dataset Reading
    doc = {}
    N = 1
    limit = 95271
    with open("../dataset/democratvsrepublicantweets/output.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(N)
            if N == limit:
                break

            if row[0] == "Republican":
                doc[N] = preprocess(row[2])
                doc[N].append("real republican")
                N += 1
            elif row[0] == "Democrat":
                doc[N] = preprocess(row[2])
                doc[N].append("real democrat")
                N += 1
            else:
                continue

    # with open("../dataset/russian-troll-tweets/IRAhandle_tweets_1.csv", newline='') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         if N == limit*2:
    #             break

    #         if row[len(row)-1] == "RightTroll":
    #             doc[N] = preprocess(row[2])
    #             doc[N].append("fake republican")
    #             N += 1
    #         elif row[len(row)-1] == "LeftTroll":
    #             doc[N] = preprocess(row[2])
    #             doc[N].append("fake democrat")
    #             N += 1
    #         else:
    #             continue

    # Term Frequency
    corpus = {}
    for d in doc:
        for w in doc[d]:
            if " " in w:
                continue
            elif w in corpus:
                corpus[w][d] += 1
            else:
                corpus[w] = {}
                for i in range(N):
                    corpus[w][i+1] = 0
                corpus[w][d] = 1


    # Vector Space
    if not os.path.exists("vector_space.csv"):
        with open('../vector_space.csv', 'w', newline='') as csv_td:
            writer = csv.writer(csv_td)
            writer.writerow(list(corpus.keys()))
            for i in range(N):
                d = int(i)
                row = []
                for w in corpus:
                    row.append(corpus[w][d])
                writer.writerow(row)

# preprocess of document
def preprocess( doc ):
    preprocessed = tokenize(doc)

    skip = ["RT"]
    preprocessed = [ w for w in preprocessed if w not in skip and "http" not in w ]

    preprocessed = normalize(preprocessed)
    preprocessed = lemmatize(preprocessed)
    preprocessed = stem(preprocessed)

    return preprocessed

# tokenization of document
def tokenize( doc ):

    # tokenizing
    tokenized = word_tokenize(doc)

    return tokenized

# normalization and filtration of document
def normalize( tokenized ):

    #normalizing
    # normalized = [ unidecode.unidecode(w.decode('utf8')) for w in tokenized ]

    # remove punctuations
    normalized = [ word for word in tokenized if word.isalpha() ]

    # removing stopwords
    stop_words = set(stopwords.words('english'))
    filtered = [ w for w in normalized if w not in stop_words ]

    return filtered

# lemmatization of document
def lemmatize( tokenized ):
    lemmatizer = WordNetLemmatizer()
    lemmatized = [ lemmatizer.lemmatize(w) for w in tokenized ]
    return lemmatized

# stemming of document
def stem( tokenized ):
    stemmer = PorterStemmer()
    stemmed = [ str(stemmer.stem(w)) for w in tokenized if is_ascii(str(stemmer.stem(w))) ]
    return stemmed

def is_ascii(s):
    return all(ord(c) < 128 for c in s)


if __name__ == "__main__":
    main()