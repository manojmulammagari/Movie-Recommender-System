# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI(title="Movie Recommender API")

# 1. Load the precomputed data into memory when the server starts
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 2. Define the expected structure of the user's request
class MovieRequest(BaseModel):
    title: str

# 3. Create the recommendation endpoint
@app.post("/recommend")
def recommend_movie(request: MovieRequest):
    # Check if the movie exists in our database
    if request.title not in movies['title'].values:
        raise HTTPException(status_code=404, detail="Movie not found in database.")
    
    # Find the index of the requested movie
    movie_index = movies[movies['title'] == request.title].index[0]
    
    # Get the similarity scores for this movie and sort them
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    # Retrieve the titles of the top 5 recommended movies
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return {"movie": request.title, "recommendations": recommended_movies}