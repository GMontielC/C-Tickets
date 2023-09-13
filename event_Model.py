from pydantic import BaseModel

class event (BaseModel):
    id_evento: str
    category: str
    date: str
    image: str
    name: str
    meta: str
    meta2: str