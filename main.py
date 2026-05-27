from fastapi import FastAPI, Request
from mockData import products
from dtos import productDTO


app = FastAPI()


@app.get("/")
def home():
    return "Welcome to fastapi!"


@app.get("/products")
def get_products():
    return products


# path params..
# http://0.0.0.0:8000/product/2/26
@app.get("/product/{product_id}/{date}")
def get_one_product(product_id: int, date: int):

    # if product available with the id and date, return product else return error message

    for oneProduct in products:
        if oneProduct.get("id") == product_id and oneProduct.get("date") == date:
            return oneProduct

    return {
        "error": "product not found"
    }


# querry params
# http://0.0.0.0:8000/greet?name=ajay&age=26

@app.get("/greet")
def greet_user(name:str, age:int):
    return{
        "greet":f"hello {name}, your age is {age}"

    }


# i can pass n numner of  query parameters
# http://0.0.0.0:8000/greets?name=ajay  
@app.get("/greets")
def greet_users(request: Request):
    query_params = dict(request.query_params)
    print(query_params)

    return {
        "greet": f"hello {query_params.get('name')}"
    }



# diffrent types of http methods 

@app.post("/create_product")
def create_product(data:productDTO):
    # to save data in dict 
    data = data.model_dump()
    products.append(data)


    return{"status":"product created succsfully", "data":products}



# with this we can handel the data manuplation
##   pydentic  ##







# how to call different http Methods. - any tool?
# POSTMAN

# how to validate data. - DTOS. 



