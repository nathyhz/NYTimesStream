import streamlit as st
import numpy as np
import pandas as pd
import functions
from wordcloud import WordCloud
import matplotlib.pyplot as plt



# PART A: THE STORIES API

st.title("COP 4813 - Web Application Programming")
st.write("\n")
st.title("Project 1")
st.header("Part A - The Stories API")
st.write("This app uses the Top Stories API to display the most common words used in the top current\n"
         "articles based on a specified topic selected by the user. The data is displayed as a line chart and\n"
         "as a wordcloud image.")


st.subheader("I - Topic Selection")
user_input = st.text_input("Please enter your name")


option = st.selectbox(
    "Select a topic of interest",
    ["", "arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider", "magazine",
     "movies", "nyregion", "obituaries", "opinion", "politics", "realestate", "science", "sports", "sundayreview",
     "technology", "theater", "t-magazine", "travel", "upshot", "us", "world"]
)

# if both name and topic are selected
if option and user_input:
    st.write("Hello ", user_input, ". You selected the {} topic.".format(option))

    # adds users option to url and saves it to json file
    str1 = functions.url_name(option)

    st.subheader("II - Frequency Distribution")

    if st.checkbox("Click here to generate frequency distribution"):
        # calls to return top 10 words of selected topic
        item = functions.frequencyDis(str1)
        item = pd.DataFrame(item)
        df = pd.DataFrame({"words": item[0], "count": item[1]})
        import plotly.express as px
        fig = px.line(df, x="words", y="count", title='')
        st.plotly_chart(fig)

    st.subheader("III - WordCloud")
    if st.checkbox("Click here for wordcloud"):
        # generates wordcloud
        wordcloud = WordCloud().generate(str1)
        text = plt.figure(figsize=(12, 12))
        plt.imshow(wordcloud)

        plt.axis("off")
        plt.show()
        st.pyplot(text)




# PART B: MOST POPULAR ARTICLES


st.header("Part B - Most Popular Stories")
st.write("Select if you want to see the most shared, emailed, or viewed articles")

article = st.selectbox(
    "Select your preferred set of articles",
    ["", "shared", "emailed", "viewed"]
)
period = st.selectbox(
    "Select the period of time(last days)",
    ["", "1", "7", "30"]
)
 # if preferred article and period of time selected
if article and period:

    # adds article and date period to url and saves to json
    popular = functions.mostPop(article, period)

    freq = functions.frequencyDis(popular)
    wordcloud2 = WordCloud().generate(popular)
    text2 = plt.figure(figsize=(12, 12))
    plt.imshow(wordcloud2)

    plt.axis("off")
    plt.show()
    st.pyplot(text2)




