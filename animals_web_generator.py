import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """
    Serializes an animal. Fields are omitted from the output if they
    don't exist in the input dictionary.
    """
    output = ""
    output += '<li class="cards__item">\n'

    # Füge den Titel nur hinzu, wenn 'name' existiert.
    if 'name' in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    # Sicherer Zugriff auf das 'characteristics'-Dictionary.
    # .get() ist hier nützlich, um einen Fehler zu vermeiden, falls 'characteristics' fehlt.
    characteristics = animal.get('characteristics', {})

    # Füge die Diät nur hinzu, wenn sie in 'characteristics' existiert.
    if 'diet' in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    # Füge den Ort nur hinzu, wenn 'locations' existiert und nicht leer ist.
    if 'locations' in animal and animal['locations']:
        output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    # Füge den Typ nur hinzu, wenn er in 'characteristics' existiert.
    if 'type' in characteristics:
        output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    """ Main function """
    animals_data = load_data('animals_data.json')
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    with open("animals_template.html", "r", encoding="utf-8") as datei:
        inhalt = datei.read()

    inhalt = inhalt.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as datei:
        datei.write(inhalt)


if __name__ == "__main__":
    main()
