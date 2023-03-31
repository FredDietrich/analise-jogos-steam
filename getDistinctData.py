#!/usr/bin/python3

import pandas as pd
import numpy as np

df = pd.read_csv('inputData/games_data.csv', delimiter=',', low_memory=False, index_col="id")

uniqueDevs= df['developer'].nunique()
uniquePubs = df['publisher'].nunique()
uniqueTitles =  df['title'].nunique()
releaseDateCount = df['release_date'].count()
genres = df['genres'].nunique()
multiplayer = (df['multiplayer_or_singleplayer'] == 'CA').values.sum()

genres_list_all = df['multiplayer_or_singleplayer'].str.split(';').dropna().to_numpy()
genres_list_unique = np.unique(sum(genres_list_all, []))

#Single Player
print('Single-player games:', df['multiplayer_or_singleplayer'].str.contains('Single-player').sum())

#MultiPlayer
print('Multi-Player games: ', df['multiplayer_or_singleplayer'].str.lower().str.contains('multi-player').sum())

overall_review_list_unique = df['overall_review'].dropna().unique()
print('Overall Review', overall_review_list_unique)

detailed_review_list_unique = df['detailed_review'].dropna().unique()
print('Detailed Review', len(detailed_review_list_unique))


print('Unique titles: ', uniqueTitles)
print('Unique developers: ', uniqueDevs)
print('Unique publishers: ', uniquePubs)
print('Release dates', releaseDateCount)
print('genres', genres)
print('Unique multiplayer/singleplayer values', len(genres_list_unique))
