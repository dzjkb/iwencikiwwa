import json
import pandas as pd

iwenciki = pd.read_csv('iwenciki.csv', dtype=str).to_dict('records')
with open('iwenciki.json', 'w') as f:
    json.dump({"event_list": iwenciki}, f)