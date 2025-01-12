from sqlmodel import SQLModel


class ResponseModel(SQLModel):
    code: int
    message: str
    data: dict | None | list | str | int | float = None