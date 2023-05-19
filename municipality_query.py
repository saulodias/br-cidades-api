import warnings
import geopandas as gpd
from shapely.geometry import Point


class MunicipalityQueryBase:
    def __init__(self, data_file):
        self.load_map_data(data_file)

    def load_map_data(self, file_path):
        raise NotImplementedError(
            "Subclasses must implement load_map_data method")

    async def query_municipality(self, latitude, longitude):
        raise NotImplementedError(
            "Subclasses must implement query_municipality method")


class MunicipalityQueryGenerator(MunicipalityQueryBase):
    def load_map_data(self, file_path):
        self.map_data = gpd.read_file(file_path)

    async def query_municipality(self, latitude, longitude):
        warnings.warn(
            "MunicipalityQueryList is about 7 times faster than MunicipalityQueryGenerator, and is recommended if memory usage is not an issue.", DeprecationWarning)

        point = Point(longitude, latitude)
        for _, municipality in self.map_data.iterrows():
            if municipality.geometry.contains(point):
                return {"uf": municipality.SIGLA_UF, "city": municipality.NM_MUN}
        return None


class MunicipalityQueryList(MunicipalityQueryBase):
    def load_map_data(self, file_path):
        self.map_data = list(gpd.read_file(file_path).to_dict('records'))

    async def query_municipality(self, latitude, longitude):
        point = Point(longitude, latitude)

        for municipality in self.map_data:
            if municipality['geometry'].contains(point):
                return {"uf": municipality['SIGLA_UF'], "city": municipality['NM_MUN']}
        return None
