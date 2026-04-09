import streamlit as st
import pickle
import joblib
import nltk
import sklearn
import pandas as pd


st.title('Movie Recommendation System')
with open("movies.pickle","rb") as f:
    movies = pickle.load(f)


similarity = joblib.load('similarity.joblib','rb')

movies_names = movies['title'].values
# movie_name = st.text_input('Enter Movie Name')




def recommend(name_movie):
    movie_index = movies[movies == name_movie].index[0]
    movie_list = similarity[movie_index]
    movie_list = sorted(list(enumerate(movie_list)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title) 
    return recommended_movies#[:5]



name_movie = st.selectbox('Enter Movie Name',movies_names)

if st.button('Recommend'):
    r = recommend(name_movie)
    
    st.write('Recommended Movies are:')
    for i in r:
        st.write(i)