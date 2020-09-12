import csv
import json
import pathlib
import glob

current_folder = pathlib.Path(__file__).parent.absolute()
organisation_files = glob.glob(
    f"{current_folder}/organisations_geocoded/*_coded.csv")

for organisation_file in organisation_files:
    organisation_name = pathlib.Path(
        organisation_file).name.replace("_coded.csv", "")
    data = []
    with open(organisation_file, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            def null_if_empty(key):
                if row[key] == "":
                    row[key] = None
            null_if_empty("note")
            null_if_empty("lon")
            null_if_empty("lat")
            row["container"] = int(row["container"])
            data.append(row)

    with open(f"{current_folder.parent}/public/{organisation_name}.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
