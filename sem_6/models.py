from pydantic import BaseModel, Field


class Tovar(BaseModel):
    id: int
    name: str = Field(title="Name", max_length=32)
    price: float = Field(title="Price", gt=0, le=100000)
    description: str = Field(default=None, title="Description", max_length=1000)


class User(BaseModel):
    id: int
    username: str = Field(title="Username", max_length=50)
    full_name: str = Field(None, title="Full Name", max_length=100)
    email: str = Field(max_length=128)


class Order(BaseModel):
    id: int
    dt: str = Field(max_length=32)
    tovar_id: int
    user_id: int
