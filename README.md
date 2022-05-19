# API Contatos

API para salvar contatos em um banco de dados. Utilizando a linguagem de programação **[Python](https://python.org)** e a API na estrutura **[API Fast.](https://fastapi.tiangolo.com/)**

<h1>1. Requisitos</h1>

Para a construção dessa API, foi utilizado os seguintes requerimentos:

<ul style="list-style-type: circle">
    <li><a href='https://fastapi.tiangolo.com/' target='_blank'>FastAPI</a> Biblioteca estrutural desta API <code>$ pip install fastapi </code></li>
    <li><a href='https://www.uvicorn.org/' target='_blank'>Uvicorn</a> Servidor de testes <code>$ pip install uvicorn["standard"] </code></li>
    <li><a href='http://docs.peewee-orm.com/en/latest/' target='_blank'>Peewee</a> Python Database ORM <code>$ pip install peewee </code></li>
</ul>

> **Observação 1.0:** Nesse projeto se encontra o arquivo [```requirements.txt```](requirements.txt), nele você encontra toda a lista de dependências para o projeto. Para instalar, apenas digite: **```$ pip install -r requirements.txt```**.

<h1>2. Models</h1>

<p>
    No diretório <code>/core/models</code> você pode encontrar dois arquivos distintos:
</p>

<ul style="list-style-type: circle">
    <li>
        <a href='/core/models/contatos.py' target='_blank'>Contatos</a>
        - Essa classe é um modelo para um json com dados requeridos para fazer operações.
        <ul style='list-style-type: none'>
            <li>
                <code style='color: #ff0000'>
                    <div>
                        name: string <br>
                        email: string <br>
                        mobile: string <br>
                        tag: string
                    </div>
                </code>
            </li>
        </ul>
    </li>
    <li>
        <a href='/core/models/' target='_blank'>TbContatos</a>
        - Essa classe é um modelo para entidade de um banco de dados.
        <ul style='list-style-type: none'>
            <li>
                <code style='color: #ff0000'>
                    <div>
                        id: int (primary key)<br>
                        name: string <br>
                        email: string <br>
                        mobile: string <br>
                        tag: string
                    </div>
                </code>
            </li>
        </ul>
    </li>
</ul>

> **Observação 1.1:** Os dados de Contatos devem ser passados para TbContatos se os dados forem validados com sucesso. Isso é feito na terceira camada.

<h1>3. Estrutura do Backend</h1>

<p>
Nessa seção você irá ver como o backend do projeto foi feito e a sua comunicação. Foi utilizado uma arquitetura em camadas para essa comunicação, que consiste em:
</p>

<dl>
    <dt>
        1º Nível: <a href='/core/facade/facade.py' target='_blank'>Facade</a>
    </dt>
        <dd>
            # Os dados são enviados para cá a parti da requisição   Http desejada.
        </dd>
        <dd>
            # Tudo começa aqui, os dados são inseridos num modelo e enviados para cá, onde é feita a comunicação com o <strong style='color: red'>Service</strong>, que é o 2º Nível.
        </dd>
        <dd>
            # Cada método, cabeçalho igual os métodos do Service, deve retornar o <code>json</code> para o <i>endpoint</i>, que é a URL que pede acesso ao backend.
        </dd>
        <dd>
            # Para a realização de buscas, atualização e deleção, podem ser enviados dados de tipo primitivo, como inteiro ou string.
        </dd>
    <dt>
        2º Nível: 
        <a href='/core/service/service.py' target='_blank'>Service</a>
    </dt>
        <dd>
            # Essa classe recebe dados a partir do <strong style='color: red'>Facade</strong>, então deve fazer as validações necessárias, de acordo com o caminho desejado. e então enviar os dados para o 
            <strong style='color: red'>DAOContatos</strong>, que é o 3º Nível.
        </dd>
        <dd>
            # Todas as validações cruciais são feitas por meio do módulo <a href='/core/utils/validators.py' target='_blank'>validators</a>, com todas as funções e recursos de programação funcional.
        </dd>
        <dd>
            # Se for encontrado algum problema na validação, deve retornar um <code>json</code> com o <code>status code</code> e uma mensagem de erro.
        </dd>
        <dd>
            # Caso a validação esteja Ok, deve ser feita a comunicação com o <strong style='color: #ff0000'>3º Nível</strong>, que retornará um <code>json</code>, então deve voltar para o <strong style='color: #ff0000'>1º Nível</strong> que é o Facade.
        </dd>
    <dt>
        3º Nível: 
        <a href='/core/dao/dao_contatos.py' target='_blank'>DAOContatos</a>
    </dt>
        <dd>
            # Recebe dados do <strong style='color: red'>Service</strong>, um nível anterior, e processa os dados para as operações 
        </dd>
        <dd>
            # Essa classe é responsável por realizar operações de <strong style='color: red'>CRUD</strong> com os daos recebidos. Ela se comunica com o 4º Nível, que é através de um singleton em <strong style='color: red'>Database</strong>, para abrir e fechar conexão.
        </dd>
    <dt>
        4º Nível: 
        <a href='/core/persist/persist.py' target='_blank'>Database</a>
    </dt>
        <dd>
            # Essa classe utiliza o padrão <code>singleton</code> para:
        </dd>
        <dd>
            - <code>open_it()</code>Verificar Conexão já aberta, se não existir, criar uma e verificar arquivo <code>conftest.json</code> para selecionar o banco de dados entre o de teste e o oficial. Ou então, fechar conexão com <code>close_it()</code>.
        </dd>
        <dd>
            # Retornar ou Fechar uma Conexão
        </dd>
        <dd>
            # Comunica com o <strong style='color: red'>3º Nível</strong> para as tarefas solicitadas.
        </dd>
        <dd>
            # Comunica com o modelo de entidade <a href='/core/models/tb_contatos.py' target='_blank'>TbContatos</a>
        </dd>
</dl>

> **Observação 1.2:** Nesta estrutura do backend, é possível acessar pelo Facade. Cada metódo encontrado no Facade é correspondete a uma requisição HTML ```[ post, get, update, delete ]```.

<h2>3.1. Estrutura das Pastas</h2>

<p>
Nessa área você poderá ver a estrutura dos pacotes e diretórios.
</p>

```
contatos-fast -> diretório raiz.
|    core > pacote com as operações backend.
|    |    dao > pacote com o arquivo de dao (crud).
|    |    |   __init__.py
|    |    |   dao_contatos.py
|    |    facade > pacote com o facade ou controller.
|    |    |   __init__.py
|    |    |   facade.py
|    |    models > pacote com os modelos.
|    |    |   __init__.py
|    |    |   contatos.py
|    |    |   tb_contatos.py
|    |    persist > pacote para configurar banco de dados.
|    |    |   __init__.py
|    |    |   persist.py
|    |    service > pacote com a regra de negócio.
|    |    |   __init__.py
|    |    |   service.py
|    |    utils > pacote com módulos auxiliares.
|    |    |   __init__.py
|    |    |   config.py
|    |    |   validators.py
|    |    __init__.py
|    settings > diretório com arquivo configuração.
|    main.py # arquivo principal
|    README.md # esta documentação.
|    requirements.txt # dependências.
|    routes.py # url configuration.
--------------------------------------------------------<>
```

<h1>
4. Considerações Finais
</h1>

<p>
***
Esse projeto é apenas para mostrar a habilidade de fazer uma API Fast, portanto os dados e possíveis inconsitências não serão tratados a parti desse pequeno projeto.
</p>
