import csv
import json
import pathlib

current_folder = pathlib.Path(__file__).parent.absolute()

data = []
with open(f"{current_folder}/caritas_coded.csv", "r", encoding="utf-8") as csv_file:
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

with open(f"{current_folder}/caritas.json", 'w', encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)
