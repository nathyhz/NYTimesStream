import json
import requests
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import main_functions
from wordcloud import WordCloud
import matplotlib.pyplot as plt



api_key_dict = main_functions.read_from_file("JSON_Files/API_KEY.json")
api_key = api_key_dict["my_key"]

# generates link with selected topic
def url_name(topic):
    url = "https://api.nytimes.com/svc/topstories/v2/{0}.json?api-key=".format(topic)
    url = url + api_key
    response = requests.get(url).json()
    main_functions.save_to_file(response, "JSON_FILES/response.json")
    my_articles = main_functions.read_from_file("JSON_Files/response.json")
    str1 = ""
    for i in my_articles["results"]:
        str1 = str1 + i["abstract"]
    return str1


# gathers frequency of 10 most common words
def frequencyDis(str1):

    words = word_tokenize(str1)

    words_no_punc = []
    for w in words:
        if w.isalpha():
            words_no_punc.append(w.lower())

    notwords = stopwords.words("english")

    clean_words = []
    for w in words_no_punc:
        if w not in notwords:
            clean_words.append(w)

    freqDist3 = FreqDist(clean_words)
    return freqDist3.most_common(10)


# generates link with both preferred set of articles as well as period of time to be saved onto json file
def mostPop(option1, option2):
    url = "https://api.nytimes.com/svc/mostpopular/v2/{0}/{1}.json?api-key=".format(option1, option2)
    url = url + api_key
    response = requests.get(url).json()
    main_functions.save_to_file(response, "JSON_FILES/response.json")
    popArticles = main_functions.read_from_file("JSON_Files/response.json")
    str1 = ""
    for i in popArticles["results"]:
        str1 = str1 + i["abstract"]
    return str1


