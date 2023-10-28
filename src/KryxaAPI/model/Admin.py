from pydantic import BaseModel, Field
from typing import Annotated, Literal


class Admin(BaseModel):
    AdminID: Annotated[int, Field(ge=0)]
    Fullname: Annotated[str, Field(max_length=100, min_length=1)]
    Phone: Annotated[str, Field(min_length=1)]
    Password: Annotated[str, Field(min_length=1)]