from flask import Flask, request, jsonify
import numpy as np
import pickle
import pandas as pd
import json

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    pickle_model = pickle.load(file)

with open("finalfeatures.txt", "r") as f:
        data_str = f.read()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([json.loads(data)])
    data = eval(data_str)
    sample = df[data]


    prediction = pickle_model.predict(sample)
    data = [
    (0, 'Adware'),
    (1, 'Backdoor'),
    (2, 'Banker'),
    (3, 'Benign'),
    (4, 'Dropper'),
    (5, 'FileInfector'),
    (6, 'NoCategory'),
    (7, 'PUA'),
    (8, 'Ransomware'),
    (9, 'Riskware'),
    (10, 'SMS'),
    (11, 'Scareware'),
    (12, 'Spy'),
    (13, 'Trojan'),
    (14, 'Zeroday')
    ]
    

    for k, v in data:
        if k == prediction:
            value = v
            break
    

    response = {'prediction': value}
    

    print("Done")
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
