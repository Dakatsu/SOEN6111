# Project Summary

Our project will implement a content-based recommendation system in order to suggest games an existing user of the Steam video game digital distribution system may enjoy playing. The system will base its recommendations on an analysis of a large (168GB +) collection of data about the games available in the Steam library and how they relate to games the user already has. The Steam game library of a particular user, along with statistics on how long they have played the game, can be retrieved from Steam itself using its public APIs.

The dataset contains information on over 74,000 games available in the Steam library. Data that will likely be very predictive include the genre, category tags, Metacritic score, description, and price. However, this project will also investigate the predictive quality of other attributes like publisher, price, release date, and the number of preview images and videos on the store page.

Our content-based recommendation system requires constructing a user profile based on their interactions with games they already own or have played, including their hours played and any reviews they wrote. This user profile will allow our models to rate other games based on their item profiles, which will be composed of the aforementioned attributes from the data set along with what can be retrieved from the API.

This project will produce answers for two questions:
* What attributes from the dataset should have the most pronounced impact on predictions?
* How can we recommend the most appropriate games for an existing Steam user?

The recommendation system will use and compare two different algorithms: cosine similarity and random forest.
* Cosine Similarity requires creating vectors of data for every game in the dataset, then it calculates the distance between the vectors for games the user owns and vectors for possible recommendations. Shorter distances suggest better recommendations.
* Random Forest uses a variety of decision trees that each return a boolean (yes/no) answer to whether the game should be recommended to the user. All of these results are combined to give a single score that determines the confidence in the result.

The root-mean-square error (RMSE) method will be used at the end of the project to evaluate the quality of the models.
