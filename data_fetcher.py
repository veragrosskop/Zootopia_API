import requests


API_KEY = "7RsAC8SWkL7GF8ETySbC4wkDnUHflEX2PDag6cqx"


def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """

  payload = {'X-Api-Key': API_KEY}
  r = requests.get(f"https://api.api-ninjas.com/v1/animals?name={animal_name}", params=payload)
  return r.json()