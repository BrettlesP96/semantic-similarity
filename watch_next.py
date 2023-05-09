import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MOVIES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movies.txt")
planet_hulk_description = ("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

def read_movies_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return [line.strip().replace(" :", "|", 1) for line in lines]


def find_similar_movie(description, movies):
    vectorizer = TfidfVectorizer()
    movie_descriptions = [description] + movies
    tfidf_matrix = vectorizer.fit_transform(movie_descriptions)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    most_similar_index = np.argmax(cosine_similarities)
    return movies[most_similar_index].split("|", 1)[0]


if __name__ == "__main__":
    movie_descriptions = read_movies_file(MOVIES_FILE)
    similar_movie_title = find_similar_movie(planet_hulk_description, movie_descriptions)
    print(f"The most similar movie to watch next is {similar_movie_title}")
