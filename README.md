## DATA SCIENCE HENRY -  Individual Project 1 - Movies API ##

### 1) Project Objetives ###
+ The project consists of creating an ETL from two given movie datasets. Make an EDA of the data. Create an ML model for the data recommendation. And finally implement and deploy an API in the cloud with some request data functions.

### 3) Programming Language and Libraries ###
- Programming language: 
  - Python 3
- Main Libraries: 
  - Flask
  - pandas
  - nltk
  - seaborn
  - scikit-learn




### 2) Files & Folders ###
+ \ETL.ipynb - ETL python notebook
+ \EDA.ipynb - EDA python notebook
+ \reco_model.ipynb - Recomendation Model python notebook 
+ \app.py - Main python flask API
+ \testapi.sh - Bash script to test API from console
+ \data\ - Folder with data files used by the project
+ \templates - Flask templates

### 3) Links ### 




### 4) API Functions Resume ###
+ def **peliculas_idioma( *`Language`: str* )**:
  Return quantity of movies in the given language

+ def **peliculas_duracion( *`Movie`: str* )**:
  Returns movie runtime and release year

+ def **franquicia( *`Collection`: str* )**:
  Returns movie quantity and revenues

+ def **peliculas_pais( *`Country`: str* )**:
  Returns quantity of movies produced by a given country

+ def **productoras_exitosas( *`Productora`: str* )**:
  Returns revenue and quantity of movies of a given company

+ def **get_director( *`Director`: str* )**
  Returns director success and list of movies from the given director
+ def **recomendaciones( *`Movie`: str* )**
  Returns 5 similar movies from the given one


### 8) Addional INFO ###
+ Author: Flavio Bovio
+ Start/End: 2023-07-24 / 2023-08-11