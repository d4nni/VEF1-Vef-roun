from flask import Flask, json

app = Flask(__name__)

# Parsing JSON
@app.route('/')
def index():

    # dictionary
    d = {
        'first_name': 'Guido',
        'second_name': 'Rossum',
        'titles': ['BDFL', 'Developer']
    }

    # convert dictionary to JSON (string containing JSON)
    # dumps fyrir strengi, dump fyrir skrár
    json_string_data = json.dumps(d)

    # '{"first_name": "Guido", "last_name": "Rossum", "titles": ["BDFL", "Developer"]}'
    print(json_string_data)

    return json_string_data 

app.run(debug=True)

