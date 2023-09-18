from annoy import AnnoyIndex


def build_annoy_index(vector_size: int, index_path: str, metric="euclidean"):
    annoy_index = AnnoyIndex(vector_size, metric=metric)
    annoy_index.load(index_path)
    return annoy_index
