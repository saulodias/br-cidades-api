import geopandas as gpd
from shapely.geometry import Point
from flask import Flask, jsonify


def load_map_data():
    global map_data
    map_data = gpd.read_file('BR_Municipios_2022.zip')


def query_municipality(latitude, longitude):
    point = Point(longitude, latitude)
    for _, municipality in map_data.iterrows():
        if municipality.geometry.contains(point):
            return {"uf": municipality.SIGLA_UF, "city": municipality.NM_MUN}
    return None

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@app.route('/city/<coordinates>', methods=['GET'])
def query(coordinates):
    latitude, longitude = coordinates.split(',')
    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return jsonify({"message": "Valores de latitude e longitude inválidos."})

    result = query_municipality(latitude, longitude)
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Nenhum município encontrado para as coordenadas dadas."})

if __name__ == '__main__':
    load_map_data()  # Load map data once at the start
    app.run() # Test server
