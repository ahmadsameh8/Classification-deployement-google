
# Load the dataset and preprocess it
import pandas as pd
import json
import requests
data = pd.read_csv("randomSample.csv")

X = data.iloc[1].to_dict()


json_data = json.dumps(X)


url = "http://127.0.0.1:5000/predict"



response = requests.post(url,json=json_data)

print(response.json())