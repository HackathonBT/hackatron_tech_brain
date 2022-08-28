from fastapi import APIRouter
from app.api.loading.loading_file import load_file
from app.api.check.check import check


api_router = APIRouter()


api_router.add_api_route(
    path='/loading',
    endpoint=load_file,
    methods=['POST'],
    tags=['other']
)

api_router.add_api_route(
    path='/check',
    endpoint=check,
    methods=['POST'],
    tags=['other']
)
