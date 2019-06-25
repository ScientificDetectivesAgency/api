# from models import Department as DepartmentModel
from models import Entidad as EntidadModel
# from models import Employee as EmployeeModel
# from models import Role as RoleModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Entidad(SQLAlchemyObjectType):
    class Meta:
        model = EntidadModel
        interfaces = (relay.Node, )


# class Employee(SQLAlchemyObjectType):
#     class Meta:
#         model = EmployeeModel
#         interfaces = (relay.Node, )


# class Role(SQLAlchemyObjectType):
#     class Meta:
#         model = RoleModel
#         interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_entidad = SQLAlchemyConnectionField(Entidad)
    # Disable sorting over this field
    


schema = graphene.Schema(query=Query, types=[Entidad])
