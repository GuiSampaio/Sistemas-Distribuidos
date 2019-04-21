from socket import  *
import threading
import sys

def recebe():
        while True:
                data = s.recv (4096)

                print (data.decode('UTF-8'))     

def envia():
        while True:

                mensagem = input ("Digite a msg!: ")  

                if(mensagem != None):
                        s.send(str.encode(mensagem, "UTF-8"))
        s.close ()                       

s = socket ()


servidor="192.168.0.112"
porta=8752

s.connect((servidor, porta))
t1 = threading.Thread(target=envia, args=())
t = threading.Thread(target=recebe,args=())
t1.start()
t.start()

