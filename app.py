import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
import requests
import zipfile
import io

url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))

movies = pd.read_csv(z.open("ml-latest-small/movies.csv"))

# Clean it
movies = movies[['movieId','title','genres']]
movies = movies.rename(columns={"genres":"feature"})
movies.dropna(inplace=True)

books = pd.DataFrame({
    "title":["The Hobbit","Harry Potter","Da Vinci Code","Pride and Prejudice"],
    "feature":["Fantasy","Fantasy","Thriller","Romance"]
})

restaurants = pd.DataFrame({
    "name":["Dominos","Spice Hub","Sushi Place","Olive Garden"],
    "feature":["Italian","Indian","Japanese","Italian"]
})

# Model
vectorizer = TfidfVectorizer(stop_words='english')
matrix = vectorizer.fit_transform(movies['feature'])

def recommend(idx):
    sim = cosine_similarity(matrix[idx], matrix).flatten()
    indices = sim.argsort()[::-1][1:6]
    return movies.iloc[indices]

def cross_domain(idx):
    genre = movies.iloc[idx]['feature']
    return {
        "books": books.sample(2)['title'].tolist(),
        "restaurants": restaurants.sample(2)['name'].tolist()
    }

# UI
st.title("🎯 UniRec - Smart Recommendation System")

selected = st.selectbox("Choose a movie", movies['title'].head(200))

if st.button("Recommend"):
    idx = movies[movies['title']==selected].index[0]
    
    st.subheader("🎬 Similar Movies")
    recs = recommend(idx)
    st.write(recs['title'].values)

    cross = cross_domain(idx)
    
    st.subheader("📚 Books")
    st.write(cross['books'])

    st.subheader("🍽️ Restaurants")
    st.write(cross['restaurants'])