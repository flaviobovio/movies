import os
from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)




df_movies = pd.read_parquet('data/movies_acotado.pq')


@app.route('/')
def index():
    return render_template('index.html')    


@app.route('/peliculas_idioma/<idioma>', methods=['GET'])
def peliculas_idioma(idioma:str):

    mask = df_movies.original_language == idioma
    cantidad = len(df_movies[mask])
    respuesta = {'language' : idioma, 'quantity': cantidad}

    return json.dumps(respuesta)


@app.route('/peliculas_duracion/<pelicula>', methods=['GET'])
def peliculas_duracion(pelicula:str):

    pelicula = pelicula.title()
    peli = df_movies[df_movies.title == pelicula]    
    if len(peli)==1:
        duracion = round(peli['runtime'].values[0])
        anio = round(peli['release_year'].values[0])
    else:
        pelicula = f'Error: {pelicula} does not exists' 
        duracion = anio = 0

    respuesta = {'Movie':pelicula, 'Runtime' : duracion, 'year' : anio}

    return json.dumps(respuesta)



@app.route('/franquicia/<franquicia>', methods=['GET'])
def franquicia(franquicia:str):
    franquicia = franquicia.title()
    pelis = df_movies[df_movies.belongs_to_collection == franquicia]
    cantidad = len(pelis)

    if cantidad>0:
        ganancia = round(pelis.revenue.sum())
        promedio = round(ganancia / cantidad)        
    else:
        franquicia = f'Error: {franquicia} does not exists'
        ganancia = promedio = 0

    respuesta = {'collection' : franquicia, 'quantity' : cantidad, 'revenue': ganancia, 'average' : promedio}
    
    return json.dumps(respuesta)



@app.route('/peliculas_pais/<pais>', methods=['GET'])
def peliculas_pais(pais:str):
    mask = df_movies.production_countries.str.contains("'"+pais+"'", case=False)
    producciones = len (df_movies[mask])
    respuesta = {'country':pais, 'productions':producciones}

    return json.dumps(respuesta)




@app.route('/productoras_exitosas/<productora>', methods=['GET'])
def productoras_exitosas(productora:str):
    mask = df_movies.production_companies.str.contains(productora, case=False)
    producciones = df_movies[mask]
    if len(productora)>0:
        total_revenue = round(producciones.revenue.sum())
        cantidad = len(producciones)
    else:
        total_revenue = 0 
        cantidad = 0

    respuesta = {'company': productora, 'total_revenue':total_revenue, 'total_movies':cantidad}

    return json.dumps(respuesta)



@app.route('/get_director/<director>', methods=['GET'])
def get_director(director:str):
    director = director.title()
    pelis = df_movies[df_movies.director==director]
    retorno = round(pelis['return'].sum(), 2)
    detalle = [{'movie':v, 'date':w, 'return':x, 'budget': y, 'revenue':z} \
            for v, w, x, y, z in zip(pelis['title'], pelis['release_date'],\
                                    pelis['return'], pelis['budget'], pelis['revenue'])]

    respuesta = {'director': director, 'total_return':retorno, 'detail':detalle}

    return json.dumps(respuesta)




@app.route('/recomendacion/<pelicula>', methods=['GET'])
def recomendaciones(pelicula:str):
    pelicula = pelicula.title()
    peli = df_movies[df_movies.title == pelicula]
    if len(peli)==1:
        recomendations = list(peli.iloc[0].recomendations)
    else:
        pelicula = f'Error: {pelicula} does not exists' 
        recomendations = {}

    respuesta = {'Movie':pelicula, 'Recomendations' : recomendations}

    return json.dumps(respuesta)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
