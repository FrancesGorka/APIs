from fastapi import FastAPI, HTTPException
import uvicorn

api = FastAPI()

products = []

@api.post('/products/add')
def add_product(product: str):
    if not product:
        raise HTTPException(status_code=400, detail='Product name is required')
    
    products.append(product)
    return {'message': 'Product added successfully!', 'products': products}

if __name__ == '__main__':
    uvicorn.run(api, port=5000, host='0.0.0.0')
