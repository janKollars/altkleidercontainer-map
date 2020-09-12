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
    def set_coordinates(toAdd):
            address["lon"] = toAdd["lon"]
            address["lat"] = toAdd["lat"]


    if not (address["lon"] and address["lat"]):
        response = requests.get(
                f"https://nominatim.openstreetmap.org/search.php?street={address['street']}&city={address['city']}&state={address['state']}&country=Austria&polygon_geojson=1&format=jsonv2"
        )
        response_data = response.json()

        for result in response_data:
            house_found = False
            if result["type"] == "house":
                house_found = True
                set_coordinates(result)
            if house_found:
                break
            else:
                set_coordinates(response_data[0])

with open(f"{current_folder}/caritas_coded.csv", mode="w") as csv_file:
    writer = csv.DictWriter(
        csv_file,
        fieldnames=["state", "postal", "city", "street", "container", "note", "lon", "lat"],
        delimiter=";"
    )

    writer.writeheader()
    for address in data:
        writer.writerow(address)
