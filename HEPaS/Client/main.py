import time

from Module.oust_hepa_client import ClientApplication
from Module.Socket import ClientSocket
from Module.Display_output import print_course_info , print_unit_marks_table

HEADER = 64
FORMAT = 'utf-8'

Server_Port = 9090
Server_Address = "192.168.1.2"

def main():

    

    client_socket = ClientSocket(Server_Address, Server_Port, FORMAT, HEADER)

    client_socket.client_connect()

    try:

        while True:

            try:

                app = ClientApplication()

                app.prompt_OUST_status()

                OUST_status = app.get_OUST_status()

                if OUST_status == "yes":

                    oust_person = app.prompt_personal_info_OUST()

                    client_socket.client_send(OUST_status, oust_person)

                    # client Recieve 
                    print_course_info(client_socket.receive_string_data(), client_socket.receive_string_data(), client_socket.receive_string_data()) 

                    print_unit_marks_table(client_socket.receive_json_data())


                if OUST_status == "no":

                    person_id =  app.prompt_personal_info_non_OUST() 

                    non_oust_units = app.prompt_unit_mark_non_oust()

                    decision = app.count_repeating_units()

                    if decision == "Not eligible for Honors":
                    
                        print(f"{person_id} is not eligible for honors")

                    if decision == "for further assessment":    

                        client_socket.client_send(OUST_status, non_oust_units)

                        # client Recieve 
                        print_course_info(client_socket.receive_string_data(), client_socket.receive_string_data(), client_socket.receive_string_data()) 

                        print_unit_marks_table(client_socket.receive_json_data())

            except Exception as e:

                print(f"Error: {e}")


            # Ask the user if they want to end the connection
            user_response = input("Do you want to end the connection? (yes/no): ").lower()

            if user_response == "yes":

                break  # Exit the loop and end the connection

            # Add a delay before reconnecting to the server
            time.sleep(5)  # 5 seconds delay, adjust as needed

    except KeyboardInterrupt:

        print("User interrupted. Closing the connection.")

    finally:

        client_socket.client_disconnect()  # Close the socket connection

    

if __name__ == "__main__":
    main()
