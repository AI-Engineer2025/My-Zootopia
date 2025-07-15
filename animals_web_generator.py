import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')



for animal in animals_data:
  print("Name:",animal["name"],"\n"
        "Diet:",animal["characteristics"]["diet"],"\n"
        "Location:",animal["locations"][0],"\n"
        "Type:",animal["taxonomy"]["class"],
        "\n")