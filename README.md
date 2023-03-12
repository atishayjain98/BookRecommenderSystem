# Book Recommender System

## Description 
Designing a system that suggests a variety of books to users by taking into account their interests.

## Dataset
For our project, we utilized the Book-Crossing Dataset, which is composed of three tables: 
- Books 
- Users
- Ratings 

The Books table contains 8 columns, including ISBN, Book title, Book author, Year of publication, Publisher, and three columns for Book cover Image URLs (small, medium, and large). 

The Users table contains information about the users, including their UserID, Location, and age. 

The Ratings table contains data on book ratings, including UserID, ISBN, and Book Rating.

## PreProcessing and Cleaning 

Here is a summary of the pre-processing and cleaning steps performed on the Dataset:

For the Books table -- 
- The three Image URL features were dropped
- The null values in the table (only 3) were replaced with 'Other'.
- Invalid entries in the year column were fixed by manually setting the values for three tuples using their ISBN number, converting the type of the years of publications feature to an integer, and replacing all invalid years with the mode of the publications.

For the Users table -- 
- Null values in the Age column were replaced with the mean of valid ages.
- Location column was split into three different columns (City, State, and Country) with 'Other' assigned as the entity value in the case of null value.
- Invalid ages in the Age column were also replaced by keeping the valid age range of readers as 10 to 80.

For the Ratings table --  
- Null values was checked
- Punctuation was removed from ISBN column values. Only the ISBNs that were available in the book dataset were considered, and the alphabets present in the ISBN column were upper-cased.


Finally, all three tables were merged, and tuples having ratings of 0 were dropped from the final dataset.

## Algorithms Included

### 1. Popularity-Based Recommendation:
Based on the total ratings received by the books in the whole collection, a specific place, or yearly.

### 2. User-Item Collaborative Filtering Recommendation:
Considers user ratings to find cosine similarities and recommend books.
Considers books with at least 50 ratings.

### 3. Content-Based Recommendation:
Recommends books based on similarities in book titles.
Creates TF-IDF feature vectors for unigrams and bigrams of book titles.
Considers books with at least 80 ratings.

### 4. Hybrid Approach (Collaborative+Content) Recommendation:
Combines the results of collaborative and content-based filtering systems using a percentile score.
Recommends top n books.


The libraries used in the implementation include :
- ipython-notebook
- scikit-learn
- seaborn
- matplotlib
- numpy
- scipy
- pandas












