import os
from datetime import datetime
import json
import csv
import requests


url = "https://services.arcgis.com/iFBq2AW9XO0jYYF7/ArcGIS/rest/services/Covid19byZIPnew/FeatureServer/0/query"

field_names_list = [
    "ZIPCode",
    "Cases",
    "Deaths",
    "TotalPop",
    "Place",
    "Note"
]

params = {
    "where": "1=1",
    "returnGeometry": False,
    "outFields": field_names_list,
    "f": "json"
}

r = requests.get(url, params)
r_json = r.json()
feature_data = r_json['features']


now = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
outfile = os.path.join(os.getcwd(), 'nc_zip', f'{now}.csv')
with  open(outfile, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(field_names_list)
    for feature in feature_data:
        row = []
        for field in field_names_list:
            row.append(feature['attributes'][field])  
        writer.writerow(row)