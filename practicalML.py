import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Task 1
basics = pd.read_csv('title.basics.tsv', sep='\t')
ratings = pd.read_csv('title.ratings.tsv', sep='\t')
most_voted = ratings[ratings.numVotes > 100]
movies = basics[basics.titleType == 'movie']
most_voted_movies = most_voted[most_voted.tconst.isin(movies.tconst)]
most_voted_movies.hist(column='averageRating')

# plot result
f1 = plt.figure(1)
plt.xlabel('ratings')
plt.ylabel('number of movies')


# Task 2
tv_series = basics[basics.titleType == 'tvSeries']
tv_series = tv_series[(tv_series.startYear != '\\N') & (tv_series.endYear != '\\N')]
tv_series.startYear = tv_series.startYear.astype(str).astype(int)
tv_series.endYear = tv_series.endYear.astype(str).astype(int)
production_length = tv_series['endYear'].sub(tv_series['startYear'], axis=0)

# plot result
f2 = plt.figure(2)
production_length.hist()
plt.xlabel('total production period in years')
plt.ylabel('number of shows')


# Task 3
# select all movies and join ratings to them
ratings = ratings[ratings.tconst.isin(movies.tconst)]
movies = ratings.join(movies.set_index('tconst'), on='tconst')

# separate movies based on relevant genre
m_comedy = movies[movies.genres.str.contains('Comedy', na=False)]
m_western = movies[movies.genres.str.contains('Western', na=False)]
m_drama = movies[movies.genres.str.contains('Drama', na=False)]
m_fantasy = movies[movies.genres.str.contains('Fantasy', na=False)]
m_doc = movies[movies.genres.str.contains('Documentary', na=False)]

# mean rating for each genre
r_comedy = m_comedy.averageRating.mean()
r_western = m_western.averageRating.mean()
r_drama = m_drama.averageRating.mean()
r_fantasy = m_fantasy.averageRating.mean()
r_doc = m_doc.averageRating.mean()

# plot result
f3 = plt.figure(3)
genres = ('Comedy', 'Western', 'Drama', 'Fantasy', 'Documentary')
y_pos = np.arange(len(genres))
avg_ratings = [r_comedy, r_western, r_drama, r_fantasy, r_doc]

plt.bar(y_pos, avg_ratings, align='center')
plt.xticks(y_pos, genres)
plt.ylabel('average rating')

plt.show()