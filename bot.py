from faker import Faker
from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

from produto import Produto

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def instanciar_produto(nome: str, preco: float, qtd: int):
    return Produto(nome, preco, qtd)


def listar_produtos(produtos: list):
    for produto in produtos:
        print(produto)
    

def processar_produto(produto: dict):
    nome = produto['nome']
    preco = produto['preco']
    qtd = produto['qtd']
    
    obj_produto = instanciar_produto(nome, preco, qtd)
    escrever_produto(obj_produto.__str__(), 'produtos.txt')
    
    
def escrever_produto(produto: Produto, nome_arquivo: str):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(produto + '\n') 


def inventar_produtos(quantidade: range):
    fake = Faker()
    produtos = []
    for _ in quantidade:
        nome = f'{fake.word().capitalize()} {fake.word().capitalize()}'
        preco = fake.random_number(digits=3)
        qtd = fake.random_number(digits=2)
        
        produtos.append({"nome": nome, "preco": preco, "qtd": qtd})
    
    return produtos


def preencher_forms(bot: WebBot, produtos: list):
    for produto in produtos:
        bot.browse('http://127.0.0.1:5000')
        bot.wait(1000)
        
        input_nome = bot.find_element('//*[@id="nome"]', By.XPATH)
        input_preco = bot.find_element('//*[@id="preco"]', By.XPATH)
        input_qtd = bot.find_element('//*[@id="qtd"]', By.XPATH)
        btn_submit = bot.find_element('/html/body/div/form/input[4]', By.XPATH)
    
        input_nome.send_keys(produto["nome"])
        input_preco.send_keys(produto["preco"])
        input_qtd.send_keys(produto["qtd"])
        
        btn_submit.click()
        bot.wait(1000)

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    try:
        produtos = inventar_produtos(range(10))
        listar_produtos(produtos)
        preencher_forms(bot, produtos)
    
    except Exception as ex:
        print(ex)
        
    finally:
        pass


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
