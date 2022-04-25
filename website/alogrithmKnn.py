# -*- coding: utf-8 -*-
import pickle

import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
# %matplotlib inline


movies = pd.read_csv('Data/movies.csv')


movies.sample(10)

ratings = pd.read_csv('Data/ratings.csv')
ratings.head()

combine_movie_rating= pd.merge(ratings,movies,on='movieId')
combine_movie_rating=combine_movie_rating.drop(['timestamp'],axis = 1)
combine_movie_rating.head()

combine_movie_rating = combine_movie_rating.dropna(axis = 0 ,subset=['title'])
combine_movie_rating.head()

movie_rating_count=pd.DataFrame(combine_movie_rating.
                    groupby(['movieId'])['rating'].
                    count().
                    reset_index().
                    rename(columns={'rating':'totalRatingCount'})                   
                   )
movie_rating_count.head()

pd.set_option('display.float_format', lambda x: '%.3f' % x)


rating_with_totalRatingCount = combine_movie_rating.merge(movie_rating_count,left_on='movieId',right_on='movieId')
rating_with_totalRatingCount.head()

#10% of the movies have more than 158 reviews
popular_threshold=158
rating_popular_movies= rating_with_totalRatingCount.query('totalRatingCount>=@popular_threshold')
rating_popular_movies.head()

ratings_pivot = rating_popular_movies.pivot(index='movieId', columns='userId',values='rating').fillna(0)
ratings_pivot_sparse = csr_matrix(ratings_pivot.values)

model_nn_binary = NearestNeighbors(metric='cosine', algorithm='brute')
model_nn_binary.fit(ratings_pivot_sparse)

with open("train.csv", 'ab') as f:
    for x in range(1, movies.shape[0]):
        try:
            if (movies['movieId'] == x).any():
                movieId = x
                currentmovie = " "
                movielist = []
                distances, indices = model_nn_binary.kneighbors(ratings_pivot.query('movieId == ' + str(x)).values,
                                                                n_neighbors=11)
                for i in range(0, len(distances.flatten())):
                    likelymovieId = ratings_pivot.index[indices.flatten()[i]]
                    if i == 0:
                        currentmovie = movies[movies.movieId == movieId]['title'].values[0]
                    else:
                        movielist.append(movies[movies.movieId == likelymovieId]['title'].values[0])
                result = pd.DataFrame([[movieId, currentmovie, movielist]])
                result.to_csv(f, header=False, index=False)
        except ValueError:
            pass





