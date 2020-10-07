from socket import *
need_to_run = True

def send_request_to_server (client_socket):
    global need_to_run
    request = input ("Choose two numebers to add (write game over to quit) : ")
    if request == "game over":
        need_to_run = False
    request += "\n"
    client_socket.send(request.encode())

def read_respons_from_server (client_socket):
    respons = client_socket.recv(100).decode()
    print("Respons fra server: ", respons)

def close_conection (client_socket):
    client_socket.close()
    print("Disconnected from server")

def start_client ():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("localhost", 5678))
    print("Connected to server")

    while need_to_run:
        send_request_to_server(client_socket)
        read_respons_from_server(client_socket)

    close_conection(client_socket)

if __name__ == "__main__":
    start_client()