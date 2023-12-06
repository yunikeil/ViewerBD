import json

import uvicorn
from fastapi import FastAPI

from database import engine, Base
from routers import user
import configuration


Base.metadata.create_all(bind=engine)
ROUTETRS = [user]

app = FastAPI(
    version="0.0.0",
    title="...",
    summary="...",
    openapi_tags=json.loads(open("_locales/tags_metadata.json", "r").read()), 
    docs_url="/control/docs",
    redoc_url="/control/redocs",
    openapi_url="/control/openapi.json"
)

for part in ROUTETRS:
    app.include_router(part.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host=configuration.server_ip, port=configuration.server_port, reload=True)
