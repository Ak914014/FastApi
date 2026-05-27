from pydantic import BaseModel



class productDTO(BaseModel):
    id:int
    title:str
    testing:str = "none"
    price:int =0
    count:int = 0
    date:int = 0