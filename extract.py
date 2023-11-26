from time import sleep
from datetime import datetime
import requests


def get_datetime_str(for_filename=False):
    # get date/time to be used for logging, as part of file name and exported CSV data
    if for_filename:
        datetime_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    else:
        datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return datetime_str


def get_csv_line_from_entry(entry):
    # format CSV output line from dictionary
    line = f"{entry['datetime']};{entry['velocity']};{entry['latitude']};{entry['longitude']}"
    line += "\n"
    return line


if __name__ == '__main__':
    refresh_interval = 2  # refresh interval in seconds; the map seems to refresh every 10 seconds
    location_api_url = "https://railnet.oebb.at/api/gps"
    velocity_api_url = "https://railnet.oebb.at/api/speed"

    filename = "journey_started_" + get_datetime_str(True) + ".csv"
    with open(filename, 'w') as f:
        while True:
            sleep(refresh_interval)

            # get updated current date/time to be used for logging, as part of file name and exported CSV data
            datetime_str = get_datetime_str()
            entry = {
                'datetime': datetime_str,
                'velocity': None,
                'latitude': None,
                'longitude': None
            }
            try:
                print(f"[{datetime_str}] ", end="")

                r = requests.get(url=location_api_url)
                location = r.json()
                entry['latitude'] = location['Latitude']
                entry['longitude'] = location['Longitude']
                r = requests.get(url=velocity_api_url)
                entry['velocity'] = r.json()

                print(entry)  # print extracted data, stored in dictionary for debugging
                csv_line = get_csv_line_from_entry(entry)

                # write a row to the csv file
                # print(csv_line)  # may print CSV line that's going to be written
                f.write(csv_line)
                f.flush()  # directly flush the data, so that it can be accessed by another application
            except:
                f.write(csv_line)
                f.flush()  # directly flush the data, so that it can be accessed by another application
