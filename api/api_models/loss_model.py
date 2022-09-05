from datetime import datetime
from pydantic import BaseModel
from typing import List

class GetLossResponseBody(BaseModel):
    id: int
    producer_name: str
    producer_email: str
    producer_cpf:str
    crop_local:str
    harvest_date:datetime
    crop_type:str
    event_type:str

class ListLossResponseBody(BaseModel):
    entries: List[GetLossResponseBody]

class PostLossResponseBody(BaseModel):
    producer_name: str
    producer_email: str
    producer_cpf:str
    crop_local:str
    harvest_date:str
    crop_type:str
    event_type:str