import socket
import json

class Server:

    def __init__(self, Server_Address, Server_Port, FORMAT='utf-8', HEADER=64):

        self.Server_Address = Server_Address

        self.Server_Port = Server_Port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.bind((Server_Address, Server_Port))

        self.FORMAT = FORMAT

        self.HEADER = HEADER

        self.dictionary = {}

        self.string = None

        self.data_struc = None



    def server_listen(self):

        self.server.listen()

        print(f"Server is listening on {self.Server_Address}:{self.Server_Port}")



    def server_accept(self):

        client_socket, client_address = self.server.accept()

        print(f"Connected by {client_address}")

        return client_socket, client_address



    def receive_data_length(self, client_socket, data_type):

        try:

            data_length = client_socket.recv(64).decode('utf-8')

            if data_length:

                try:

                    data_length = int(data_length)

                    return data_length

                except ValueError:

                    print(f"[ERROR] Invalid {data_type} data length received")

                    return None

        except Exception as e:

            print(f"Error receiving {data_type} data length: {e}")

            return None



    def receive_string_data(self, client_socket, client_address):

        string_data_length = self.receive_data_length(client_socket, "string")

        if string_data_length is not None:

            try:

                self.string = client_socket.recv(string_data_length).decode('utf-8').strip('\"')

                if self.string in ["yes", "no"]:

                    return self.string

                
                elif self.string == "Hello, server!":

                    
                    return self.string

                else:

                    print("Invalid string data:", self.string)

            except Exception as e:

                print(f"[ERROR] Invalid string data received from {client_address}")



    def receive_json_data(self, client_socket, client_address):

        json_data_length = self.receive_data_length(client_socket, "JSON")

        if json_data_length is not None:

            try:

                json_data = client_socket.recv(json_data_length).decode('utf-8')

                self.data_struc = json.loads(json_data)

                return self.data_struc

            except ValueError:

                print(f"[ERROR] Invalid JSON data received from {client_address}")



    def server_receive(self, client_socket, client_address):

        try:

            if client_socket:

                string = self.receive_string_data(client_socket, client_address)

                data_struc = self.receive_json_data(client_socket, client_address)

                return string, data_struc

        except Exception as e:

            print(f"Error in server_receive: {e}")



    def send_string_data(self, client_socket, string_data):

        try:

            json_string_data = json.dumps(string_data)

            string_data_length = len(json_string_data)

            string_data_length_bytes = str(string_data_length).encode(self.FORMAT)

            string_data_length_bytes += b' ' * (self.HEADER - len(string_data_length_bytes))

            client_socket.send(string_data_length_bytes)

            client_socket.send(json_string_data.encode(self.FORMAT))

        except Exception as e:

            print(f"Error sending string data: {e}")



    def send_json_data(self, client_socket, json_data):

        try:

            json_json_data = json.dumps(json_data)

            json_data_length = len(json_json_data)

            json_data_length_bytes = str(json_data_length).encode(self.FORMAT)

            json_data_length_bytes += b' ' * (self.HEADER - len(json_data_length_bytes))

            client_socket.send(json_data_length_bytes)

            client_socket.send(json_json_data.encode(self.FORMAT))

        except Exception as e:

            print(f"Error sending JSON data: {e}")



    def server_send(self, client_socket, string_data, json_data):

        self.send_string_data(client_socket, string_data)

        self.send_json_data(client_socket, json_data)


    def server_close(self):

        self.server.close()

        










