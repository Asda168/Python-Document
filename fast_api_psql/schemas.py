from datetime import datetime
from pydantic import BaseModel, ConfigDict, field_serializer

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("created_at", "updated_at")
    def format_date(self, value: datetime | None) -> str | None:
        if value is None:
            return None
        return value.strftime("%d %B %Y")