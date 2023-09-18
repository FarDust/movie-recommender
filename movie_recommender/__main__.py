from pathlib import Path

from fastapi import FastAPI
from pandas import read_csv
from pkg_resources import get_distribution

from movie_recommender.data_management.annoy import build_annoy_index
from movie_recommender.data_management.recommendations import map_recommendations

app = FastAPI(
    title="Movie Recommender",
    description="A simple movie recommender API",
    version=get_distribution("movie_recommender").version,
)

ASSETS_PATH = Path(__file__).parents[1] / "assets"

datasets = {
    "views": read_csv(
        ASSETS_PATH / "general_view_count.csv", index_col=0, nrows=5
    ).sort_values("views", ascending=False),
    "interactions": read_csv(ASSETS_PATH / "interactions.csv", index_col=0)
    .sort_values("timestamp")
    .groupby("userId")
    .first(),
    "movies_processed": read_csv(ASSETS_PATH / "movies_processed.csv", index_col=0),
    "movies_features": read_csv(ASSETS_PATH / "movies_features.csv", index_col=0),
}


artifacts = {
    "annoy_index": build_annoy_index(
        vector_size=datasets["movies_features"].shape[1],
        index_path=str(ASSETS_PATH / "annoy_index.ann"),
    ),
}


@app.get("get_new_user_recommendation/")
def get_new_user_recommendation():
    movie_numerical_index = int(datasets["views"].iloc[0].name)
    return map_recommendations(
        numerical_index=movie_numerical_index,
        recommendations=artifacts["annoy_index"].get_nns_by_item(
            movie_numerical_index, 10
        )[1:],
        movies=datasets["movies_processed"],
        movies_features=datasets["movies_features"],
        annoy_index=artifacts["annoy_index"],
    )
