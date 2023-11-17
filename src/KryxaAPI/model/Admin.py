from pydantic import BaseModel, Field
from typing import Annotated, Literal


class Admin(BaseModel):
    Password: Annotated[str, Field(min_length=1)]