## DATA SCIENCE HENRY -  Individual Project 1 - Movies API ##

### 1) Objetives ###
+ The project consists of creating an ETL from two given movie datasets. Make an EDA of the data. Create an ML model for the data recommendation. And finally implement and deploy an API in the cloud with some request data functions.

### 2) Task Summary ###
+ ETL: data normalization, remove of duplicates or null values, creation of calculated or derived columns.
+ Creation of API with the requested functions with a minimal web interface uding Flask
+ EDA: data exploration using pandas and seaborn
+ Creation of a recomendation model for movies similarity using sklearn **Note: Due to hardware limitations, the dataset was limited to movies with release year > 1950 and sliced in United States productions and NON United States productions
+ Deploy of the API into GCP microservices using Cloud Build and Cloud Run



### 3) Programming Language and Libraries ###
- Programming language: 
  - Python 3
- Main Libraries: 
  - Flask
  - pandas
  - nltk
  - seaborn
  - scikit-learn

### 4) Files & Folders ###
+ \ETL.ipynb - ETL python notebook
+ \EDA.ipynb - EDA python notebook
+ \reco_model.ipynb - Recomendation Model python notebook 
+ \app.py - Main python flask API
+ \testapi.sh - Bash script to test API from console
+ \Dockerfile - Docker configuration 
+ \cloudbuild.yaml - Google Cloud Build configuration
+ \data\ - Folder with data files used by the project
+ \templates - Flask templates

### 5) Links ### 
+ Github link for this project [Project](https://github.com/flaviobovio/movies)
+ Original dataset used by this project [Dataset](https://drive.google.com/drive/folders/1mfUVyP3jS-UMdKHERknkQ4gaCRCO2e1v)



### 6) API Functions Resume ###
+ app.route/peliculas_idioma -> Return quantity of movies in the given language

+ app.route/peliculas_duracion -> Returns movie runtime and release year

+ app.route/franquicia -> Returns movie quantity and revenues

+ app.route/peliculas_pais -> Returns quantity of movies produced by a given country

+ app.route/productoras_exitosas -> Returns revenue and quantity of movies of a given company

+ app.route/get_director -> Returns director success and list of movies from the given director

+ app.route/recomendaciones -> Returns 5 similar movies from the given one

+ ** Note: app.route = IP or deploy link of the API

### 7) Adicional INFO ###
+ Project Start: 2023-07-24 - End: 2023-08-11
+ Author: Flavio Bovio
+ E-Mail: flavioboviovt@gmail.com
+ LinkedIn: https://www.linkedin.com/in/flavio-bovio-8900b65a/
