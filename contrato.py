from datetime import datetime
from pydantic import BaseModel, PositiveInt, EmailStr, PositiveFloat
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = 'Zapflow com Gemini'
    produto2 = 'Zapflow com ChatGPT'
    produto3 = 'Zapflow com Llama 3.0'
    
    
class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        produto (PositiveInt): nome do produto
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): categoria do produto
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum    
    



   