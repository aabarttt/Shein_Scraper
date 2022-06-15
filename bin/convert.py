import json
from bin.output_example import data

with open("../sample.json", "w") as outfile:
    json.dump(data, outfile, indent = 4)
