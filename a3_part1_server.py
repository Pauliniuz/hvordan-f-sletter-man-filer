from socket import *
need_to_run = True

def read_one_line(connection_socket):
    new_line = False
    command = ""
    while not new_line:
        character = connection_socket.recv(1).decode()
        if character == "\n" or character == "\r":
            new_line = True
        else:
            command += character
    return command

def handle_next_client(connection_socket):
    global need_to_run

    command = ""
    while command == "":
        command = read_one_line(connection_socket)
        if command == "game over":
            need_to_run = False
            respons = "See ya!"
        elif "+" not in command:
            respons = "error: I only do additions "
        elif " " in command:
            respons = "error: No spaces!"
        else:
            j = 0
            numbers = ["", ""]
            for i in range(len(command)):
                if command[i] != "+":
                    numbers[j] += command[i]
                else:
                    j += 1
            respons = int(numbers[0]) + int(numbers[1])
    connection_socket.send(str(respons).encode())

def start_server ():
    welcome_socket = socket(AF_INET, SOCK_STREAM)
    welcome_socket.bind(("", 5678))
    welcome_socket.listen(1)
    print("Server ready for client connection")

    connection_socket, client_address = welcome_socket.accept()
    print("Client connected from: ", client_address)

    while need_to_run:
        handle_next_client(connection_socket)

    welcome_socket.close()
    print("Server shutdown")


if __name__ == '__main__':
    start_server()