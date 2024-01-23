import requests
import pandas as pd
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
  response = requests.get('http://localhost:3000')
  with open('data.csv', 'w', encoding="utf-8") as f:
    f.write(response.text)
  
  df = pd.read_csv('data.csv', sep=';')
  
  for index, row in df.iterrows():
    print(f"Sending {row['ident']} vélos disponibles {row['nbvelos']}")
    producer.send('velib', row['nbvelos'].encode('utf-8'), row['ident'].encode('utf-8'))