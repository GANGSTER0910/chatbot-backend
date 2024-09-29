from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, Any, Dict

class Response(BaseModel):
    ans:str
