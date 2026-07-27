import streamlit as st
import pickle
import pandas as pd

# 1. Load the models directly into Streamlit
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 2. Recommendation Logic (Bypassing the API)
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# 3. UI/UX Design
st.title("🍿 Cinematic Matchmaker")
st.write("Discover your next favorite movie based on what you already love.")

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button("Recommend"):
    st.write("Analyzing cinematic fingerprints...")
    recommendations = recommend(selected_movie)
    
    st.success("Here are your top 5 recommendations:")
    for idx, movie in enumerate(recommendations, 1):
        st.markdown(f"**{idx}. {movie}**")