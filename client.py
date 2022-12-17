import socket


LOCALHOST = '127.0.0.1'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print('Server started')

clientConnection, clientAddress = server.accept()
print('Client' + str(clientAddress) + 'connected')
message = ''

while True:
    data = clientConnection.recv(1024)
    message = data.decode()
    if message == 'Over':
        print('Connection is Over')
        break

    print('...')
    res = 0
    operation_list = message.split()
    oprnd1 = operation_list[0]
    operation = operation_list[1]
    oprnd2 = operation_list[2]

    num1 = int(oprnd1)
    num2 = int(oprnd2)

    if operation == '+':
        res = num1 + num2
    elif operation == '-':
        res = num1 - num2
    elif operation == '*':
        res = num1 * num2
    elif operation == '/' or operation == ':':
        res = num1 / num2
    else:
        print('I dont know how to do it...')

    output = str(res)
    clientConnection.send(output.encode())

clientConnection.close()


