# Import all libraries and data 

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

data = pd.read_excel("./movie_data_new.xlsx")
data.rename(columns={'Unnamed: 0' : 'movies_id'}, inplace=True)

#Getting the single feature of 'Cast','Director','Genre','Title','Description'
columns=['Cast','Director','Genre','Title','Description']

#check for null values
data[columns].isnull().values.any()

#fill all null values 
data[columns] = data[columns].fillna('')

# Concatenate title,director,genre,description in to a single feature.
def important_features(data):
    important_features = []
    for i in range(0, data.shape[0]):
        important_features.append(data['Title'][i] 
                                  + data['Director'][i] 
                                  + data['Genre'][i]
                                  + data['Description'][i])
    return important_features

# creating a column to hold combined string 
data['important_features'] = important_features(data)

# Vectorizing to calculate similarity 
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['important_features'])
tfidf_matrix.shape

# genrating cosine similarity 

cosine_sim =  linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(data.index, index = data['Title']).drop_duplicates()


# Making our recommendation model

def get_reccomendations(title, cosine_sim = cosine_sim):
    idx = indices[title]
    #getting the similariy scores for all the movies related to that movie.
    sim_scores = list(enumerate(cosine_sim[idx]))
    # sorting based on the sim score
    sim_scores = sorted(sim_scores, key=lambda x : x[1], reverse= True)
    # taking only top 5
    sim_scores = sim_scores[1:6]
    movies_indices = [i[0] for i in sim_scores]
    # Returning top 5 similar movies 
    # movies = data['Title'].iloc(movies_indices)
    # id = data['movies_id'].iloc(movies_indices)
    movies = data.iloc[movies_indices]['Title']
    id = data.iloc[movies_indices]['movies_id']
    # dframe = pd.DataFrame({"Movies":movies, "ID":id})
    dframe = pd.DataFrame({"Movies":movies})
    dframe.reset_index(drop = True, inplace= True)
    return dframe

print(get_reccomendations('The Road'))

# data.info()
new = data.drop(columns=['Year of Release','Watch Time','Genre','Movie Rating','Metascore of movie','Director','Cast','Votes','Description'])

pickle.dump(new,open('movie_list.pkl','wb'))
pickle.dump(cosine_sim,open('similarity.pkl','wb'))
    
    
    
    

        