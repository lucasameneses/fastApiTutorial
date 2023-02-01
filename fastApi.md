# FastAPI

 Esse tutorial iria iniciar uma aplicação simples com o intuito de introduzir alguns conceitos como API e Rest

### Requesitos

1. [Python](https://www.python.org/downloads/)

### Vamo começar

1. criar uma pasta do projeto
2. criar uma environment

~~~bash
python -m venv venv
~~~

3.instalar o fastApi ultilizando o pip da sua env

~~~bash
./venv/bin/pip install fastapi uvicorn
~~~

4.crie um arquivo .py com o seguinte conteudo

~~~python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
~~~

5.no terminal rode o seguinte comando pra subir o servidor

~~~bash
uvicorn main:app --reload 
~~~

6.acesse o seguinte [link](http://127.0.0.1:8000) para acessar seu endpoint

~~~link
http://127.0.0.1:8000
~~~

7.para acessa o swagger adicione /docs no final da url

~~~link
http://127.0.0.1:8000/docs
~~~

8.agr é so ganhar dinheiro
