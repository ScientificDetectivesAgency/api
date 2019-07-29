from models import DimAgebUrbana as DimAgebUrbana
from models import DimColonia as DimColonia
from models import DimColoniaAgebUrbana as DimColoniaAgebUrbana
from models import DimColoniaLocalidadUrbana as DimColoniaLocalidadUrbana
from models import DimColoniaManzana as DimColoniaManzana
from models import DimColoniaMunicipio as DimColoniaMunicipio
from models import DimDenue as DimDenue
from models import DimEntidad as DimEntidad
from models import DimIndicador as DimIndicador
from models import DimLocalidadRural as DimLocalidadRural
from models import DimLocalidadUrbana as DimLocalidadUrbana
from models import DimManzana as DimManzana
from models import DimMunicipio as DimMunicipio
from models import FactEntidad as FactEntidad
from models import FactAgebUrbana as FactAgebUrbana
from models import FactLocalidadRural as FactLocalidadRural
from models import FactLocalidadUrbana as FactLocalidadUrbana
from models import FactManzana as FactManzana
from models import FactMunicipio as FactMunicipio

from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
import graphene
import graphene_sqlalchemy as gsqa

# DimAgebUrbana
class DimAgebUrbana(gsqa.SQLAlchemyObjectType):
    class Meta:
        model = DimAgebUrbana
        interfaces = (relay.Node, )


# DimColonia
class DimColonia(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimColonia
        interfaces = (relay.Node, )

# DimColoniaAgebUrbana
class DimColoniaAgebUrbana(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchempy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimColoniaAgebUrbana
        interfaces = (relay.Node, )

# DimColoniaEntidad
                      
# DimColoniaLocalidadUrbana
class DimColoniaLocalidadUrbana(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimColoniaLocalidadUrbana
        interfaces = (relay.Node, )

# DimColoniaManzana
class DimColoniaManzana(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimColoniaManzana
        interfaces = (relay.Node, )

# DimColoniaMunicipio
class DimColoniaMunicipio(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimColoniaMunicipio
        interfaces = (relay.Node, )
                      
# DimDenue
class DimDenue(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimDenue
        interfaces = (relay.Node, )

# DimEntidad
class DimEntidad(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimEntidad
        interfaces = (relay.Node, )                      

# DimIndicador
class DimIndicador(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimIndicador
        interfaces = (relay.Node, )
                      
# DimLocalidadRural
class DimLocalidadRural(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimLocalidadRural
        interfaces = (relay.Node, )

# DimLocalidadUrbana
class DimLocalidadUrbana(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimLocalidadUrbana
        interfaces = (relay.Node, )

# DimManzana
class DimManzana(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimManzana
        interfaces = (relay.Node, )

# DimMunicipio
class DimMunicipio(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = DimMunicipio
        interfaces = (relay.Node, )

# FactAgebUrbana
class FactAgebUrbana(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = FactAgebUrbana
        interfaces = (relay.Node, )

# FactEntidad
class FactEntidad(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = FactEntidad
        interfaces = (relay.Node, )

# FactLocalidadRural
class FactLocalidadRural(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = FactLocalidadRural
        interfaces = (relay.Node, )

# FactLocalidadUrbana
class FactLocalidadUrbana(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = FactLocalidadUrbana
        interfaces = (relay.Node, )

# FactManzana
class FactManzana(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = FactManzana
        interfaces = (relay.Node, )

# FactMunicipio
class FactMunicipio(gsqa.SQLAlchemyObjectType):
    @staticmethod
    def serialize(geom):
        return engine.scalar(geom.ST_AsText())
    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphql.language.ast.StringValue):
            return engine.scalar(geoalchemy2.func.ST_GeomFromText(node.value))
    @staticmethod
    def parse_value(value):
        return engine.scalar(geoalchemy2.func.ST_GeomFromText(value))

    class Meta:
        model = FactMunicipio
        interfaces = (relay.Node, )                      

### para todas menos spatial_ref
###  QUERY
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_dim_ageb_urbana = gsqa.SQLAlchemyConnectionField(DimAgebUrbana)
    all_dim_colonia = gsqa.SQLAlchemyConnectionField(DimColonia)
    all_dim_colonia_localidad_urbana = gsqa.SQLAlchemyConnectionField(DimColoniaLocalidadUrbana)
    all_dim_colonia_manzana = gsqa.SQLAlchemyConnectionField(DimManzana)
    all_dim_colonia_municipio = gsqa.SQLAlchemyConnectionField(DimColoniaMunicipio)
    all_dim_denue = gsqa.SQLAlchemyConnectionField(DimDenue)
    all_dim_entidad = gsqa.SQLAlchemyConnectionField(DimEntidad)
    all_dim_indicador = gsqa.SQLAlchemyConnectionField(DimIndicador)
    all_dim_localidad_rural = gsqa.SQLAlchemyConnectionField(DimLocalidadRural)
    all_dim_localidad_urbana = gsqa.SQLAlchemyConnectionField(DimLocalidadUrbana)
    all_dim_manzana = gsqa.SQLAlchemyConnectionField(DimManzana)
    all_dim_municipio = gsqa.SQLAlchemyConnectionField(DimMunicipio)
    all_fact_ageb_urbana = gsqa.SQLAlchemyConnectionField(FactAgebUrbana)
    all_fact_entidad = gsqa.SQLAlchemyConnectionField(FactEntidad)
    all_fact_localidad_rural = gsqa.SQLAlchemyConnectionField(FactLocalidadUrbana)
    all_fact_localidad_urbana = gsqa.SQLAlchemyConnectionField(FactLocalidadUrbana)
    all_fact_manzana = gsqa.SQLAlchemyConnectionField(FactManzana)
    all_fact_municipio = gsqa.SQLAlchemyConnectionField(FactMunicipio)

schema = graphene.Schema(query = Query)
