#!/usr/bin/env python

from database import db_session
from flask import Flask
from schema import schema
from flask_graphql import GraphQLView

app = Flask(__name__)
app.debug = True

example_query = """
{
  allEntidades(sort: [entidad_cvegeo]) {
    edges {
      node {
        entidad_cvegeo
        name
        department {
          id
          name
        }
        role {
          id
          name
        }
      }
    }
  }
}
"""

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    #db_session.remove()
    print('Aqui no pude')

if __name__ == "__main__":
    app.run()
