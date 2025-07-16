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
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
    output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
    output += f'      <strong>Type:</strong> {animal["taxonomy"]["class"]}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
print(output)

with open("animals_template.html", "r", encoding="utf-8") as datei:
    inhalt = datei.read()

inhalt = inhalt.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as datei:
    datei.write(inhalt)
