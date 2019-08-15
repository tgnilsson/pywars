import swapi
import json
import sys

# valid episode numbers
episodes = ['1', '2', '3', '4', '5', '6', '7']

def get_ship_data(epiosde):
    # get the film from the episode number
    film = swapi.get_film(epiosde)

    # get the starships in the film
    starships = film.get_starships()

    film_data = {}
    starships_data = {}

    # get all the pilots for each starship
    for ship in starships.iter():
        pilots = ship.get_pilots()
        pilots_data = []

        # get the pilot names
        for pilot in pilots.iter():
            pilots_data.append(pilot.name)
        
        # set up the starship data with a list of pilots for each starship
        starships_data[ship.name] = {"pilots": pilots_data}

    # add the starship data to the film data
    film_data = {film.title: {"starships": starships_data}}

    # format as json
    return json.dumps(film_data)


# validate there is one arg that is a number 1 - 7, then get the data
if len(sys.argv) == 2 and sys.argv[1] in episodes:
    ship_data = get_ship_data(sys.argv[1])
    print(ship_data)
else:
    print("Please provide a number 1-7, indicating the epiosde you would like to use")
