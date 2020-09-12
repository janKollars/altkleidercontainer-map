import csv
import requests
import pathlib
import glob
from progressbar import printProgressBar

current_folder = pathlib.Path(__file__).parent.absolute()
organisation_files = glob.glob(
    f"{current_folder}/organisations/*.csv")

for organisation_file in organisation_files:
    organisation_name = pathlib.Path(
        organisation_file).name.replace(".csv", "")
    data = []

    with open(organisation_file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            data.append(row)

    print(f"Retrieving coordinates for {organisation_name}")
    for i, address in enumerate(data):
        def set_coordinates(toAdd):
            address["lon"] = toAdd["lon"]
            address["lat"] = toAdd["lat"]

        if not (address["lon"] and address["lat"]):
            response = requests.get(
                f"https://nominatim.openstreetmap.org/search.php?street={address['street']}&city={address['city']}&state={address['state']}&country=Austria&polygon_geojson=1&format=jsonv2"
            )
            response_data = response.json()

            if len(response_data) == 0:
                print(f"\n!!! Could not find coordinates of {address['street']}")

            for result in response_data:
                house_found = False
                if result["type"] == "house":
                    house_found = True
                    set_coordinates(result)
                if house_found:
                    break
                else:
                    set_coordinates(response_data[0])

        printProgressBar(i + 1, len(data), prefix="Progress:", suffix="Complete", length=50)

    with open(f"{current_folder}/organisations_geocoded/{organisation_name}_coded.csv", mode="w") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=["state", "postal", "city", "street", "container", "note", "lon", "lat"],
            delimiter=";"
        )

        writer.writeheader()
        for address in data:
            writer.writerow(address)
