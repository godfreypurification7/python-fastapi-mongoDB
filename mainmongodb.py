from fastapi import FastAPI
from routes.route import router
app=FastAPI()
app.include_router(router)




# https://cloud.mongodb.com/v2/692a80fb888f5c48e4f33d83#/overview?automateSecurity=true&connectCluster=Cluster-fastapi