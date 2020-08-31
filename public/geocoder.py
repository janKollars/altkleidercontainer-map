import csv
import requests
import pathlib

current_folder = pathlib.Path(__file__).parent.absolute()

data = []

with open(f"{current_folder}/caritas.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    for row in csv_reader:
        data.append(row)

for address in data:
    def add_coordinates(toAdd):
            address["lon"] = toAdd["lon"]
            address["lat"] = toAdd["lat"]

    if address["street"] == "Am Hofgartl 1":
        add_coordinates({
            "lon": 16.464477,
            "lat": 48.1551172
        })
    elif address["street"] == "Baron-Karl-Gasse 7":
        add_coordinates({
            "lon": 16.3526552,
            "lan": 48.1538041
        })
    elif address["street"] == "Blebanngasse/Schrutkagasse":
        add_coordinates({
            "lon": 16.2768665,
            "lat": 48.1838004
        })
    elif address["street"] == "Meißauergasse 2a/1":
        add_coordinates({
            "lon": 16.438936,
            "lat": 48.248264
        })
    elif address["street"] == "Endresstraße 59/Rudolf-Zellergasse":
        add_coordinates({
            "lon": 16.283129,
            "lat": 48.147326
        })

    else:
        response = requests.get(
                f"https://nominatim.openstreetmap.org/search.php?street={address['street']}&city={address['city']}&state={address['state']}&country=Austria&polygon_geojson=1&format=jsonv2"
        )
        response_data = response.json()

        for result in response_data:
            house_found = False
            if result["type"] == "house":
                house_found = True
                add_coordinates(result)
            if house_found:
                break
            else:
                add_coordinates(response_data[0])

with open(f"{current_folder}/caritas_coded.csv", mode="w") as csv_file:
    writer = csv.DictWriter(
        csv_file,
        fieldnames=["state", "postal", "city", "street", "container", "note", "lon", "lat"],
        delimiter=";"
    )

    writer.writeheader()
    for address in data:
        writer.writerow(address)
