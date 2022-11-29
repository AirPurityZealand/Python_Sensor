from  socket import *
from textwrap import indent
from post_threading import post_thread
import requests
import json

REST_URL = "" # "https://udpexercise2rest20221101164840.azurewebsites.net"

serverPort = 10100
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")

# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/

def post_to_rest(message): #! Here we get int, so must use class
    message = message.decode()
    response = requests.post(
        f"{REST_URL}/api/AirData", json=json.loads(message) # Maybe dont need json.loads
    )
    print(response.json())
    return


def server_listen():  # Run me as post_thread
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        #print(f"clientAddress: {clientAddress}\nmessage: {message.decode()}")
        post_thread = post_thread(target=post_to_rest(message), args=message)
        post_thread.start()

listen_post_thread = post_thread(target=server_listen)
listen_post_thread.start()

