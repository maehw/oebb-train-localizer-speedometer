# README

The Python script `extract.py` extracts the current GPS position and train speed (in km/h) from the live map publicly accessible in **ÖBB railnet trains**, hence the name of the repository. It works when being connected to the train's WiFi but independent of your device's position sensor. The data is parsed periodically (every 2 seconds) and stored to a CSV file for further analysis.

![ICE Portal Karte](./doc/oebb-live-map.png)

⬇️

![CSV snippet](./doc/csv-snippet.png)

You can also run the second Python script `serve.py` using Flask in addition. It will serve the extracted data on your own website from the latest logged CSV data. Please note that it must be started using `flask --app serve run` (`python serve.py` would immediately finish execution and return).

```
$ flask --app serve run
 * Serving Flask app 'serve'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
...
```

Use your favorite web browser and go to the URL listed in the console output: http://127.0.0.1:5000

![Flask server](./doc/flask-server.png)

## How does it work?

This script automatically sends two HTTP GET requests to the API - one for speed and one for location. The source for the train speed seems to be independent of GPS - as speed still works in tunnels whereas location (obviously) doesn ot.

## Prerequisites

* Working Python3 environment with the `requests` module installed.
* Be on an ÖBB train (tested on RJX so far).
* Manually connect to WiFi "OEBB".


## Future ideas

You could also ...

* merge this with [db-ice-localizer-speedometer](https://github.com/maehw/db-ice-localizer-speedometer).
* (see other ideas there)