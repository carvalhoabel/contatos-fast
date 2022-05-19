from typing import Union
from pydantic import BaseModel


class Contatos(BaseModel):
    """JSon Model.
    """

    name: str
    email: Union[str, None] = None
    mobile: str
    tag: Union[str, None] = None
