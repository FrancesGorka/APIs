import fastapi
import uvicorn

api = fastapi.FastAPI()

products = {
    1: {'name': 't-shirt', 'price': 19.99, 'category': 'clothes'},
    2: {'name': 'stickers', 'price': 1.99, 'category': 'accessories'},
    3: {'name': 'mug', 'price': 9.99, 'category': 'kitchenware'},
    4: {'name': 'hoodie', 'price': 29.99, 'category': 'clothes'},
    5: {'name': 'cap', 'price': 14.99, 'category': 'accessories'}
}

@api.get('/products/all')
def get_all_products():
    return products

@api.get('/products/{product_id}')
def get_product_by_id(product_id: int):
    if product_id in products:
        return products[product_id]
    else:
        return {'detail': 'Product not found'}

@api.get('/products/by_category/{category}')
def get_product_by_category(category: str):
    my_dict = {}
    for key, value in products.items():
        if 'category' in value and value['category'] == category:
            my_dict[key] = value
    return my_dict

if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='0.0.0.0')
