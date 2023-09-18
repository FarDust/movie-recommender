from typing import List
from pandas import DataFrame
from annoy import AnnoyIndex


def map_recommendations(
    numerical_index: int,
    recommendations: List[int],
    movies: DataFrame,
    movies_features: DataFrame,
    annoy_index: AnnoyIndex,
):
    mapped_recommendations = []
    for recommendation in recommendations:
        movie_id = movies_features.index[recommendation]
        movie_title = movies[movies["movieId"] == movie_id]["Title"].values
        mapped_recommendations.append(
            {
                "movie_id": movie_id,
                "movie_title": movie_title[0].capitalize(),
                "movie_genres": "|".join(
                    movies[movies["movieId"] == movie_id]["genres"].values[0]
                ),
                "similarity": annoy_index.get_distance(numerical_index, recommendation),
            }
        )
    return mapped_recommendations
