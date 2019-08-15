import swapi
import json
import sys

film = swapi.get_film(sys.argv[1])
starships = film.get_starships()

film_data = {}
starships_data = {}

for ship in starships.iter():
    pilots = ship.get_pilots()
    pilots_data = []
    for pilot in pilots.iter():
        pilots_data.append(pilot.name)
    starships_data[ship.name] = {"pilots": pilots_data}

film_data = {film.title: {"starships": starships_data}}

json_data = json.dumps(film_data)

print(json_data)
