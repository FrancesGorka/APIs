import fastapi
import uvicorn
import menu
import order

api = fastapi.FastAPI()

def configure_routing():
    api.include_router(order.router)
    api.include_router(menu.router)

if __name__ == '__main__':
    configure_routing()
    uvicorn.run(api, port=8000, host='127.0.0.1')