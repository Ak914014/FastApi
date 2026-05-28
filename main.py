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


@app.put("/update_product/{product_id}")
def update_product(product_data: productDTO, product_id: int):
# enumerate in python can show the index of the data and the index and data both 
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()   ## used  model_dump beacuse i'm seding the product data direclity not in the dict form so use this 
            return{"status":"product update successfully..", "product":product_data}

    return {
        "error":"Product is not updated..."
    }


@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    
    for index, one_product in enumerate(products):
        
        if one_product.get("id") == product_id:
            deleted_product = products.pop(index)

            return {
                "status": "product deleted successfully",
                "product": deleted_product
            }

    return {
        "error": "product not found"
    }    
# with this we can handel the data manuplation
##   pydentic  ##







# how to call different http Methods. - any tool?
# POSTMAN

# how to validate data. - DTOS. 



