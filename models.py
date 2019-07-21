from database import Base, engine
from geoalchemy2 import *
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, CHAR, Boolean
from sqlalchemy.orm import backref, relationship, column_property
import geoalchemy2, geoalchemy2.shape

########################################
##############    Models  ##############
DimAgebUrbana = Base.classes.dim_ageb_urbana
DimColoniaAgebUrbana = Base.classes.dim_colonia_ageb_urbana
## DimColoniaEntidad no porque son foráneas (?)
DimColoniaLocalidadUrbana = Base.classes.dim_colonia_localidad_urbana
DimColoniaManzana = Base.classes.dim_colonia_manzana
DimColoniaMunicipio = Base.classes.dim_colonia_municipio
DimIndicador = Base.classes.dim_indicador
FactAgebUrbana = Base.classes.fact_ageb_urbana
FactEntidad = Base.classes.fact_entidad
FactLocalidadRural = Base.classes.fact_localidad_rural
FactLocalidadUrbana = Base.classes.fact_localidad_urbana
FactManzana = Base.classes.fact_manzana
FactMunicipio = Base.classes.fact_municipio

## tabla dim_colonia
class DimColonia(Base):
    __tablename__ = "dim_colonia"
    __table_args__ = {'extend_existing': True}
    colonia_geom_6362 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 6362), nullable = True)
    colonia_geom_4326 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 4326), nullable = True)
    colonia_geom_6362_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(colonia_geom_6362, 6362)))
    colonia_geom_4326_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(colonia_geom_4326, 4326)))
    
    def to_dict(self):
        data = {
            'colonia_geom_6362_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.colonia_geom_6362)),
            'colonia_geom_4326_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.colonia_geom_4326))
    }
        return data

## tabla dim_denue
class DimDenue(Base):
    __tablename__ = "dim_denue"
    __table_args__ = {'extend_existing': True}
    denue_geom_6362 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 6362), nullable = True)
    denue_geom_4326 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 4326), nullable = True)
    denue_geom_6362_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(denue_geom_6362, 6362)))
    denue_geom_4326_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(denue_geom_4326, 4326)))
    
    def to_dict(self):
        data = {
            'denue_geom_6362_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.denue_geom_6362)),
            'denue_geom_4326_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.denue_geom_4326))
    }
        return data
    
## tabla dim_entidad
class DimEntidad(Base):
    __tablename__ = "dim_entidad"
    __table_args__ = {'extend_existing': True}
    entidad_geom_6362 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 6362), nullable = True)
    entidad_geom_4326 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 4326), nullable = True)
    entidad_geom_6362_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(entidad_geom_6362, 6362)))
    entidad_geom_4326_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(entidad_geom_4326, 4326)))
    
    def to_dict(self):
        data = {
            'entidad_geom_6362_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.entidad_geom_6362)),
            'entidad_geom_4326_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.entidad_geom_4326))
    }
        return data
    
## tabla dim_localidad_rural
class DimLocalidadRural(Base):
    __tablename__ = "dim_localidad_rural"
    __table_args__ = {'extend_existing': True}
    localidad_rural_geom_6362 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 6362), nullable = True)
    localidad_rural_geom_4326 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 4326), nullable = True)
    localidad_rural_geom_6362_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(localidad_rural_geom_6362, 6362)))
    localidad_rural_geom_4326_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(localidad_rural_geom_4326, 4326)))
    
    def to_dict(self):
        data = {
            'localidad_rural_geom_6362_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.localidad_rural_geom_6362)),
            'localidad_rural_geom_4326_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.localidad_rural_geom_4326))
    }
        return data

## tabla dim_localidad_urbana
class DimLocalidadUrbana(Base):
    __tablename__ = "dim_localidad_urbana"
    __table_args__ = {'extend_existing': True}
    localidad_urbana_geom_6362 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 6362), nullable = True)
    localidad_urbana_geom_4326 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 4326), nullable = True)
    localidad_urbana_geom_6362_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(localidad_urbana_geom_6362, 6362)))
    localidad_urbana_geom_4326_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(localidad_urbana_geom_4326, 4326)))
    
    def to_dict(self):
        data = {
            'localidad_urbana_geom_6362_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.localidad_urbana_geom_6362)),
            'localidad_urbana_geom_4326_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.localidad_urbana_geom_4326))
    }
        return data

## tabla dim_manzana
class DimManzana(Base):
    __tablename__ = "dim_manzana"
    __table_args__ = {'extend_existing': True}
    manzana_geom_6362 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 6362), nullable = True)
    manzana_geom_4326 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 4326), nullable = True)
    manzana_geom_6362_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(manzana_geom_6362, 6362)))
    manzana_geom_4326_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(manzana_geom_4326, 4326)))
    
    def to_dict(self):
        data = {
            'manzana_geom_6362_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.manzana_geom_6362)),
            'manzana_geom_4326_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.manzana_geom_4326))
    }
        return data

## tabla dim_municipio
class DimMunicipio(Base):
    __tablename__ = "dim_municipio"
    __table_args__ = {'extend_existing': True}
    municipio_geom_6362 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 6362), nullable = True)
    municipio_geom_4326 = Column(
        Geometry(geometry_type='MULTIPOLYGON',srid = 4326), nullable = True)
    municipio_geom_6362_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(municipio_geom_6362, 6362)))
    municipio_geom_4326_json = column_property(
        func.ST_AsGeoJSON(func.ST_Transform(municipio_geom_4326, 4326)))
    
    def to_dict(self):
        data = {
            'municipio_geom_6362_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.municipio_geom_6362)),
            'municipio_geom_4326_json': func.ST_AsGeoJSON(
                func.ST_Transform(self.municipio_geom_4326))
    }
        return data

Base.prepare(engine, reflect = True)
