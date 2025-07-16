import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')



"""for animal in animals_data:
  print("Name:",animal["name"],"\n"
        "Diet:",animal["characteristics"]["diet"],"\n"
        "Location:",animal["locations"][0],"\n"
        "Type:",animal["taxonomy"]["class"],
        "\n")"""


output = ""  # define an empty string
for animal in animals_data:
    # append information to each string
    output += f"Name: {animal['name']}\n"
    output += f"Diet: {animal['characteristics']['diet']}\n"
    output += f"Location: {animal["locations"][0]}\n"
    output += f"Type: {animal["taxonomy"]["class"]}\n"

#print(output)

with open("animals_template.html", "r", encoding="utf-8") as datei:
    inhalt = datei.read()

inhalt = inhalt.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as datei:
    datei.write(inhalt)

print(inhalt)