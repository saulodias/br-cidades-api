import os
import asyncio
from flask import Flask, jsonify
from municipality_query import MunicipalityQueryList

data_file = 'BR_Municipios_2022.zip'
current_directory = os.path.abspath(".")
file_path = os.path.abspath(data_file)

app = Flask(__name__)
query_list = MunicipalityQueryList(file_path)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@app.route('/city/<coordinates>', methods=['GET'])
async def query(coordinates):
    latitude, longitude = coordinates.split(',')
    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return jsonify({"message": "Valores de latitude e longitude inválidos."})

    result = await query_list.query_municipality(latitude, longitude)
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Nenhum município encontrado para as coordenadas dadas."})


if __name__ == '__main__':
    app.run()
