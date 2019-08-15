## Overview

The pywars project consists of a python script that requires a single argument, a number 1-7, indicating a specific Star Wars episode. Given that argument, the script utilizes the Star Wars API to retrieve a list of all the Starships in that episode and their pilots, returned in JSON format.

## Usage

To use, be sure to `pip install -r requirements.txt`. Then simply run the script with `python main.py [1-7]`

## Docker

The script can be run from within a docker container. You can pull the docker image from tnilsson/pywars:latest, or build it youself.

There are various options for running the script from a docker container. You can run the container interactively with a shell and execute the script:

```
docker run -it tnilsson/pywars:latest /bin/sh
```

You can run the container detached and exec into the shell:

```
docker run -d --name pywars tnilsson/pywars:latest
docker exec -it pywars /bin/sh
```

You can overwrite the docker image command with the script:

```
docker run tnilsson/pywars:latest python main.py [1-7]
```

Or exec into the detached container with the script directly:
```
docker exec -it pywars python main.py [1-7]
```

## Kubernetes/Helm

If you have a local install of minikube, the helm chart can be used as well. From within the project directory:

```
helm install ./pywarschart/
```

Then use kubectl to find the pod and exec into it and run the script, similar to the docker exec commands above.
