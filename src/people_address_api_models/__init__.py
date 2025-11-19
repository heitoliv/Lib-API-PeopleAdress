from .models import Pessoa, PessoaBase, Endereco, EnderecoBase
from .dto import (
    PessoaBase as PessoaDTOBase,
    PessoaCreate,
    PessoaRead,
    PessoaUpdate,
    EnderecoBase as EnderecoDTOBase,
    EnderecoCreate,
    EnderecoRead,
    EnderecoUpdate,
    PessoaReadWithEnderecos,
)
