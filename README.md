# People API

## Descrição do Projeto

Essa API consiste em um projeto de CRUD para ser consumido localmente por alguma SPA.

## Tecnologias Utilizadas no Projeto

- Django Rest Framework para o desenvolvimento de aplicações em Python.
- API de exemplo para ser consumida.
- Banco de dados PostgreSQL.
- Swagger e OpenAPI para documentação da API.

## **Instalação**

- inicie Ambiente Virtual `venv`

```bash
python -m venv venv
```

**Ative o ambiente virtual**:

- No Windows (cmd.exe):

  ```sh
  venv\Scripts\activate.bat
  ```

- No Windows (PowerShell):

  ```sh
  venv\Scripts\Activate.ps1
  ```

- No Git Bash ou Linux/Mac:

  ```sh
  source venv/Scripts/activate
  ```

Para instalar todas as ferramentas necessárias, basta utilizar o `requirements.txt`.

```python
pip install -r requirements.txt
```

## Deixei um `.env` para você configurar suas variáveis de ambiente.

- Instale a Biblioteca

```bash
pip install python-dotenv
```

**Exemplo de como deve ficar o `.env`, precisa apenas colocar o seu caminho.**

```json
SENHA_DO_BANCO_DE_DADOS= ' admin'
```

O nome do arquivo

```vscode
.env
```

## Endpoints da API

### **Link da Documentação da API**

<br>

- [Documentação da API](http://127.0.0.1:8000/docs/)

<br>

- [Documentação da API Alternativa](http://127.0.0.1:8000/redoc/)

<br>

---

- Schema

```json
{
  "nome": "Robson Ferreira",
  "email": "rob@example.com",
  "idade": 30,
  "profissao": "Desenvolvedor",
  "salario": 3000
}
```

## License

Licença [MIT licensed](LICENSE).
