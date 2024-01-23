from kafka import KafkaConsumer

consumer = KafkaConsumer('velib', group_id='velib-nbvelos', bootstrap_servers='localhost:9092', enable_auto_commit=False)

for msg in consumer:
    print(f"Station {msg.key.decode()} : {msg.value} vélos disponibles")
    consumer.commit()