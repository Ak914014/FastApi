from fastapi import FastAPI
from mockData import products

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to fastapi!"

@app.get("/products")
def get_products():
    return products


# path params.. 

@app.get(("/product/{product_id}"))
def get_product(product_id:int):

    # if product available ttwith the id , return product , else return error message.

    product = None
    
    return {
        "count":product_id,
    }