from .models import Pessoa, PessoaBase, Endereco, EnderecoBase
from .dto import (
    PessoaBase as PessoaBaseDTO,
    PessoaCreate,
    PessoaRead,
    PessoaUpdate,
    EnderecoBase as EnderecoBaseDTO,
    EnderecoCreate,
    EnderecoRead,
    EnderecoUpdate,
    PessoaReadWithEnderecos,
)

__all__ = [
    "Pessoa",
    "PessoaBase",
    "Endereco",
    "EnderecoBase",
    "PessoaBaseDTO",
    "PessoaCreate",
    "PessoaRead",
    "PessoaUpdate",
    "EnderecoBaseDTO",
    "EnderecoCreate",
    "EnderecoRead",
    "EnderecoUpdate",
    "PessoaReadWithEnderecos",
]
