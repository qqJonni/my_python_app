from flask import Flask, request, jsonify

app = Flask(__name__)

# Пример NoSQL базы данных в виде словаря Python
db = {}


@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    db[key] = value
    return jsonify({'message': 'Значение создано успешно'})


@app.route('/update/<key>', methods=['PUT'])
def update(key):
    data = request.get_json()
    new_value = data.get('value')
    if key in db:
        db[key] = new_value
        return jsonify({'message': f'Значение для ключа {key} обновлено успешно'})
    else:
        return jsonify({'error': f'Ключ {key} не найден'})


@app.route('/read/<key>', methods=['GET'])
def read(key):
    if key in db:
        return jsonify({'value': db[key]})
    else:
        return jsonify({'error': f'Ключ {key} не найден'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
