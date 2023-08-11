#!/bin/bash
echo "\n=== Test peliculas_idioma ==="
export rq=https://my-python-app-ei4zqecxya-uc.a.run.app/peliculas_idioma/en
echo "request"
echo $rq
echo "response"
curl $rq


echo "\n\n=== Test peliculas_duracion ==="
export rq=https://my-python-app-ei4zqecxya-uc.a.run.app/peliculas_duracion/the%20terminator
echo "request"
echo $rq
echo "response"
curl $rq

echo "\n\n=== Test franquicia ==="
export rq=https://my-python-app-ei4zqecxya-uc.a.run.app/franquicia/cars%20collection
echo "request"
echo $rq
echo "response"
curl $rq

echo "\n\n=== Test peliculas_pais ==="
export rq=https://my-python-app-ei4zqecxya-uc.a.run.app/peliculas_pais/United%20States%20of%20America
echo "request"
echo $rq
echo "response"
curl $rq






echo "\n\n=== Test productoras_exitosas ==="
export rq=https://my-python-app-ei4zqecxya-uc.a.run.app/productoras_exitosas/paramount%20pictures
echo "request"
echo $rq
echo "response"
curl $rq


echo "\n\n=== Test get_director ==="
export rq=https://my-python-app-ei4zqecxya-uc.a.run.app/get_director/James%20Gunn
echo "request"
echo $rq
echo "response"
curl $rq




echo "\n\n=== Test recomendations ==="
export rq=https://my-python-app-ei4zqecxya-uc.a.run.app/recomendacion/toy%20story
echo "request"
echo $rq
echo "response"
curl $rq
echo "\n"



