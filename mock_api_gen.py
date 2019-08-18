import json
import requests

"""Python script to make a mockaroo api-call using schema from either .json or list of dicts. Writes mock data to a .json file and/or returns a list of dicts.

The function is modular, so you can remove specific if/elif/else statements to reduce code lines depending on your needs.

Limited to returning .json files but can expand to include other formats offered by mockaroo (e.g. .csv, .sql).
"""


def mock_api_gen(key, count, start_path=None, end_path=None, schema=None):
  """
        Parameters
        ----------

        NON-DEFAULT
        key : str
            Mockaroo api key
        count : int
            Number of rows to be returned
        end_path : str
            File location to write the .json file of rows
        
        DEFAULT (either schema or both start_path & end_path)
        start_path : str
            File location to read the .json containing schema for api call
        
        end_path : str
            File location to write and read the .json containing the rows from the api call
        
        schema : list of dicts
            list of dicts containing schema for api call

  """
  
  fields = []
  URL = f"https://api.mockaroo.com/api/generate.json?key={key}&count={count}"

  # if/else sets fields to list of dict from .json or local variable
  if not schema and start_path:
    with open(start_path, 'r') as f:
      fields = json.load(f)

  else:
    fields = schema  
  
  # makes api call to Mockaroo
  response = requests.post(url=URL, json=fields)
  
  # takes in schema from .json and writes rows to .json file
  if (start_path and end_path) and not schema:
    with open(end_path, 'w') as fp:
      json.dump(response.json(), fp)
    return end_path
  
  # takes in list, returns list of rows and writes rows to .json file
  elif schema and end_path:
    with open(end_path, 'w') as fp:
      json.dump(response.json(), fp)
      mock_dict = response.json()
    return mock_dict

  # returns list of rows only
  else:
    mock_dict = response.json()
    return mock_dict









