from datetime import datetime
from pydantic import BaseModel, Field, field_serializer
from typing import Annotated


class Bill(BaseModel):
    BillID: Annotated[int, Field(ge=0)]
    PcID: Annotated[int, Field(ge=0)]
    Datetime: datetime | None
    Note: Annotated[str, Field(max_length=100)]
    Total: Annotated[float, Field(default=0)]
    Cart: list[dict]

    @field_serializer('Datetime')
    def serialize_datetime(self, d: datetime):
        return d.astimezone().isoformat()
