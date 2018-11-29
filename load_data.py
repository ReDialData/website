import zipfile
import json

with zipfile.ZipFile('redial_dataset.zip', 'r') as z:
    z.extractall()

train_data = []
for line in open("train_data.jsonl", "r"):
    train_data.append(json.loads(line))
print("Loaded {} train conversations".format(len(train_data)))

test_data = []
for line in open("test_data.jsonl", "r"):
    test_data.append(json.loads(line))
print("Loaded {} test conversations".format(len(test_data)))
