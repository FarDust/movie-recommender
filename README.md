# Movie Recommender

Estoy usando distancia euclidiana dado que los embeddings de texto generados por google/flan-t5-small son de 512 dimensiones. Dado que estos vectores son una representación de la semántica de las palabras, la distancia euclidiana es una buena métrica para medir la similitud entre dos textos.

Se tomo el supuesto de que usar bag of words para el problema era lo suficientemente bueno, asi que se promediaron los embeddings de cada palabra en los distintos textos y se calculo la distancia euclidiana entre los embeddings de cada texto.

Ademas se agrego información de los géneros de las películas, dado que se considero que es un factor importante para la recomendación de películas. Ademas esto ayuda a resolver desempates entre películas que tienen la misma distancia euclidiana entre sus embeddings.

Se ignoraron ciertas variables como el año de lanzamiento de la película, director, etc. dado que complicaban el problema y no se encontró una forma de usarlas para mejorar la recomendación de manera significativa.
