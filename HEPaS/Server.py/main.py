from Module.Socket import Server
from Module.basic_operations_server import ServerBasicOperations 
from Module.HEPas_Student_validation import StudentScoresRetriever
import threading

# Create a threading lock
client_lock = threading.Lock()

def main():

    Server_Port = 9090

    Server_Address = "192.168.1.2"

    server = Server(Server_Address, Server_Port)

    server.server_listen()

    # Instantiate the class with database connection details
    scores_retriever = StudentScoresRetriever(

        host="localhost",

        user="root",

        password="Pqr#^(XYZ&*(!",

        database="testdatabase"

    )

    try:
        while True:
            # Accept a new client connection
            client_socket, client_address = server.server_accept()

            # Create a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(server, client_socket, client_address, scores_retriever))

            # Start the thread to handle the client
            client_thread.start()

    except KeyboardInterrupt:

        print("Server terminated by the user.")

    finally:

        server.server_close()

def handle_client(server, client_socket, client_address, scores_retriever):

    # Acquire the lock before processing the client
    with client_lock:

        try:

            while True:

                validate_credentials(server, client_socket, client_address, scores_retriever)


        except ConnectionResetError:

            print(f"Client {client_address} disconnected. Closing the client socket.")


        except Exception as e:

            print(f"Error processing client request from {client_address}: {e}")


        finally:

            client_socket.close()

            # Release the lock after processing the client

def validate_credentials(server, client_socket, client_address, scores_retriever):

    oust_status, dictionary = server.server_receive(client_socket, client_address)


    if oust_status == "yes":
        if 'first_name' in dictionary:

            unit_mark = scores_retriever.get_student_scores(student_id=dictionary.get('person_id'), student_email=dictionary.get('email'))

            server_operation = ServerBasicOperations()

            server_operation.process_data(unit_mark)

            server.send_string_data(client_socket, server_operation.calculate_course_average())

            server.send_string_data(client_socket, server_operation.calculate_best8_average())

            server.send_string_data(client_socket, server_operation.send_evaluation_result())

            server.send_json_data(client_socket, unit_mark)

    if oust_status == "no":

        server_operation = ServerBasicOperations()

        server_operation.process_data(dictionary)

        server.send_string_data(client_socket, server_operation.calculate_course_average())

        server.send_string_data(client_socket, server_operation.calculate_best8_average())

        server.send_string_data(client_socket, server_operation.send_evaluation_result())

        server.send_json_data(client_socket, dictionary)



if __name__ == "__main__":
    
    main()

