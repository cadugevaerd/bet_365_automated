from telethon import TelegramClient, sync, events
from time import sleep
import requests
from dotenv import load_dotenv
import os
import pyautogui as pg
import sys

SESSAO = 'Coletar dados para bot bet365'

while True:
    try:
        api_id = os.environ['api_id']
        api_hash = os.environ['api_hash']
        break
    except:
        if os.path.isfile('.env'):
            load_dotenv()
            continue
        else:
            pg.alert('Favor adicionar as variáveis de ambiente no sisitema: api_id, api_hash e bot_token', 'Erro ao ler variáveis de ambiente')
            sys.exit(1)

#client = TelegramClient('session', api_id, api_hash).start(bot_token=bot_token)

def obter_chats():
    client = TelegramClient(SESSAO, api_id, api_hash)
    client.start()
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        
        if dialog.id < 0:
            print("-"*20)
            print(f'Grupo: {dialog.title}')
            print(f'ID: {dialog.id}')
        else:
            pass
    client.disconnect()

def monitorar():
    print("Monitorando grupo...")
    client = TelegramClient(SESSAO, api_id, api_hash)
    @client.on(events.NewMessage(chats = [1001036378156]))
    async def print_mensagem(event):
        print("Nova Mensagem: " + event.message.message, flush=True)
    client.start()
    client.run_until_disconnected()
def menu():
    print("Selecione uma das opções:")
    print("1 - Listar todos os grupos disponíveis")
    print("2 - Monitorar um grupo")
    print("3 - Sair")
    opcao = input("Opção: ")

if __name__ == "__main__":
    #print(api_id, api_hash)
    #obter_chats()
    monitorar()