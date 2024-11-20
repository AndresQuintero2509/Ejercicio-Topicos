from flask import Flask, request, jsonify
import pika
import json

app = Flask(__name__)

# Ruta POST para recibir y publicar mensajes en la cola
@app.route('/publish', methods=['POST'])
def publish_message():
    # Obtener los datos del cuerpo del POST
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON inválido"}), 400

    try:

        connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='some-rabbit', port=5672))
        channel = connection.channel()

        channel.exchange_declare(exchange='pedidos', exchange_type='fanout')
        channel.queue_declare(queue='ordenes')
        channel.queue_bind(exchange='pedidos', queue='ordenes', routing_key='pedido')
        channel.queue_declare(queue='notificaciones')
        channel.queue_bind(exchange='pedidos', queue='notificaciones', routing_key='pedido')

        # Publicar el mensaje en la cola
        channel.basic_publish(
            exchange='pedidos',
            routing_key='pedido',
            body=json.dumps(data)
        )
        print(f"Mensaje enviado: {data}")

        # Respuesta de éxito
        return jsonify({"message": "Mensaje publicado correctamente", "data": data}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "No se pudo publicar el mensaje"}), 500

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)