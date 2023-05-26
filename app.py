import streamlit as st
import pickle
import pandas as pd
import requests

movies_list=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
      response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
      data=response.json()
      return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_idx=movies[movies['title']==movie].index[0]
    distances=similarity[movie_idx]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
              recommended_movies.append(movies.iloc[i[0]].title)
              recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies,recommended_movies_poster

st.title("Movie Recommender System")
movies=pd.DataFrame(movies_list)
option = st.selectbox(
'Which movie you want to watch today?',
movies['title'].values)   

if st.button('Recommnend'):
    name,posters=recommend(option)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
          st.text(name[0])
          st.image(posters[0])
    with col2:
          st.text(name[1])
          st.image(posters[1])
    with col3:
          st.text(name[2])
          st.image(posters[2])
    with col4:
          st.text(name[3])
          st.image(posters[3])
    with col5:
          st.text(name[4])
          st.image(posters[4])