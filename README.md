# API AC3

Criação de uma API com os métodos GET, POST e DELETE.

Busca de todos as informações dos alunos, inserção e exclusão no banco de dados.

Usei o Postman para fazer as requisições.

# Para o professor:

Usei o MySql com o XAMPP e criei meu próprio banco de dados:

BD - alunos

Table - info_alunos

Atributos:

ID - Auto incremental (int)

Nome (varchar)

Sobrenome (varchar)

Turma (varchar)



## Referência

 - [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)


## Autores

- [@richard P.](https://github.com/richarpaulinoT)


## Documentação da API

#### Retorna todos os itens

```http
  GET /api/registros
```

#### Cadastra um item

```http
  POST   /api/cadastro
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Nome`      | `string` | **Obrigatório**. |
| `Sobrenome`      | `string` | **Obrigatório**. |
| `Turma`      | `string` | **Obrigatório**. |

#### Deleta um item

```http
  DELETE   /api/delete-registros
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `ID`      | `string` | **Obrigatório**. |
