import socket
import json

class ClientSocket:

    def __init__(self, Server_Address, Server_Port, FORMAT='utf-8', HEADER=64):

        self.Server_Address = Server_Address

        self.Server_Port = Server_Port

        self.server_socket = (self.Server_Address, self.Server_Port)

        self.FORMAT = FORMAT

        self.HEADER = HEADER

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def client_connect(self):

        try:

            self.client.connect(self.server_socket)

        except ConnectionRefusedError as e:

            print(f"Connection refused: {e}")

        except Exception as e:

            print(f"Error: {e}")


    def send_string_data(self, string_data):
        try:
            json_string_data = json.dumps(string_data)

            string_data_length = len(json_string_data)

            string_data_length_bytes = str(string_data_length).encode(self.FORMAT)

            string_data_length_bytes += b' ' * (self.HEADER - len(string_data_length_bytes))

            self.client.send(string_data_length_bytes)

            self.client.send(json_string_data.encode(self.FORMAT))

        except Exception as e:

            print(f"Error sending string data: {e}")



    def send_json_data(self, json_data):

        try:

            json_json_data = json.dumps(json_data)

            json_data_length = len(json_json_data)

            json_data_length_bytes = str(json_data_length).encode(self.FORMAT)

            json_data_length_bytes += b' ' * (self.HEADER - len(json_data_length_bytes))

            self.client.send(json_data_length_bytes)

            self.client.send(json_json_data.encode(self.FORMAT))

        except Exception as e:

            print(f"Error sending JSON data: {e}")



    def client_send(self, string_data, json_data):

        self.send_string_data(string_data)

        self.send_json_data(json_data)



    def receive_data_length(self, data_type):

        try:

            data_length = self.client.recv(64).decode('utf-8')

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



    def receive_string_data(self):

        string_data_length = self.receive_data_length("string")

        if string_data_length is not None:

            try:

                self.string = self.client.recv(string_data_length).decode('utf-8').strip('\"')

                return self.string

            except Exception as e:

                print(f"[ERROR] Invalid string data received from {self.Server_Address}")



    def receive_json_data(self):

        json_data_length = self.receive_data_length("JSON")

        if json_data_length is not None:

            try:

                json_data = self.client.recv(json_data_length).decode('utf-8')

                self.data_struc = json.loads(json_data)

                return self.data_struc

            except ValueError:

                print(f"[ERROR] Invalid JSON data received from {self.Server_Address}")



    def client_receive(self):

        try:

            if self.client:

                string = self.receive_string_data()

                data_struc = self.receive_json_data()

                return string, data_struc

        except Exception as e:

            print(f"Error in client_receive: {e}")



    def client_disconnect(self):
        
        self.client.close()


