# Bot de Cotação do Dólar

Este projeto utiliza o conceito de orientação a objetos em _Python_ e o _Flask_ para automatizar o preenchimento de um formulário _web_, criando um objeto da classe Produto toda vez que clica no botão de Enviar. Ao final da automação, teremos um txt com todos os objetos gerados

## Início

Estas instruções detalham o fluxo que deve ser seguido para poder executar esta automação.

### Pré-requisitos
- Ter o _Python_ instalado na máquina

### Execução
* Criar um ambiente virtual para instalar as dependências:
  ```
  python -m venv venv
  venv/Scripts/Activate
  
  (venv) pip install -r requirements.txt
  ```

* Dividir o terminal do _VS Code_ (ou abrir dois terminais diferentes):
  - No primeiro terminal, rode a API:
    ```
    python app.py 
    ```
  - No segundo terminal, rode a automação:
    ```
    python bot.py
    ```