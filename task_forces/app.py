from flask import Flask, jsonify, send_from_directory, request, render_template
import random
import os

app = Flask(__name__)


dishes = {
    "pasta": "dish1.jpeg",
    "pizza": "dish2.jpg",
    "sushi": "dish3.jpg",
    "tacos": "dish4.avif",
    "burger": "dish5.jpg",
    "chole_b": "dish6.jpg",
}

image_directory = os.path.join(app.root_path, 'static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random-dish', methods=['GET'])
def random_dish():
    try:
        random_dish = random.choice(list(dishes.values()))
        return jsonify({"image": random_dish})
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching a random dish.", "details": str(e)}), 500


@app.route('/dish/<dish_type>', methods=['GET'])
def get_dish_by_type(dish_type):
    try:
        dish_type = dish_type.lower()
        if dish_type in dishes:
            return send_from_directory(image_directory, dishes[dish_type])
        else:
            return jsonify({"error": f"No dish found for type: {dish_type}"}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching the dish.", "details": str(e)}), 500


@app.route('/available-dishes', methods=['GET'])
def available_dishes():
    try:
        return jsonify(list(dishes.keys()))
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching the list of dishes.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
