from pydantic import BaseModel,ConfigDict,Field
#base model is the class that all other pydantic models will inherit from
class PostBase(BaseModel):
    title:str=Field(min_length=1,max_length=100)
    content:str =Field(min_length=1)
    author:str =Field(min_length=1,max_length=50)

class PostCreate(PostBase):
    pass
class PostResponse(PostBase):
    model_config=ConfigDict(from_attributes=True)

    id:int
    date_posted:str#in memory date is stored as string ,it should be datetime when we use database