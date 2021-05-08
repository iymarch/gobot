import graphene

from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from query import QueryCourse, Mutation

app = FastAPI()
app.add_route("/", GraphQLApp(
    schema=graphene.Schema(
        query=QueryCourse, 
        mutation=Mutation)
    )
)
