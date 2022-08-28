import logging
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.router import api_router


logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)
app.include_router(api_router, prefix="/npl")


@app.on_event('startup')
async def on_startup():
    print('Starting')
