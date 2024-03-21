from pydantic import BaseModel, Field


class UserList(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    gender: str
    create_at: str
    status: str
