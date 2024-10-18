from datetime import datetime
from pydantic import BaseModel, PositiveInt, EmailStr, PositiveFloat
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = 'Zapflow com Gemini'
    produto2 = 'Zapflow com ChatGPT'
    produto3 = 'Zapflow com Llama 3.0'
    
    
class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum    
    



   