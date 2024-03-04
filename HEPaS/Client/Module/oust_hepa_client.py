from collections import Counter

class ClientApplication:

    def __init__(self):

        self.is_OUST_student = None

        self.person_id = None

        self.first_name = None

        self.last_name = None

        self.email = None

        self.unit_code = None

        self.mark = None

        self.unit_occurence = None

        self.No_units = 0  # Initialize No_units to 0

        self.units = []  # Initialize units to an empty list

        self.failed_units = {} # Initialize failed units to an empty dictionary

        self.oust_person = {} # Initialize oust student to an empty dictioanry


    def prompt_OUST_status(self):

        while True:

            self.is_OUST_student = input("Are you an OUST student? (yes/no): ")

            if self.is_OUST_student.lower() in ['yes', 'no']:

                break

            else:

                print("Invalid input. Please enter 'yes' or 'no'.")


    def prompt_person_id(self):

        while True:

            person_id = input("Enter your Person ID: ")

            if len(person_id) == 8 and person_id.isdigit():

                return person_id

            else:

                print("Invalid Person ID. Please enter an 8-digit number.")


    def prompt_email(self):

        while True:

            email = input("Enter your OUST email address: ")

            if '@' in email and '.' in email:

                return email

            else:

                print("Invalid email address. Please enter a valid email.")


    def prompt_personal_info_OUST(self):
        
        if self.is_OUST_student.lower() == 'yes':
            
            self.person_id = self.prompt_person_id()
            
            self.first_name = input("Enter your first name: ")
            
            self.last_name = input("Enter your last name: ")
            
            self.email = self.prompt_email()

            # Update the dictionary with the new information
            self.oust_person = {

                "person_id": self.person_id,

                "first_name": self.first_name,

                "last_name": self.last_name,

                "email": self.email

            }

        return self.oust_person
    
            

    def prompt_personal_info_non_OUST(self):

        if self.is_OUST_student.lower() == 'no':

            self.person_id = self.prompt_person_id()


        return self.person_id


    def prompt_mark(self, unit_code):

        while True:

            mark = input(f"Enter the {unit_code} Mark: ")

            if mark.isdigit() and 0 <= int(mark) <= 100:

                return int(mark)

            else:

                print("Invalid mark. Please enter a number between 0 and 100.")


    def prompt_unit_mark_non_oust(self):

        while self.No_units < 30:

                self.unit_code = input("Enter unit (or press enter to finish): ")

                if self.unit_code == '':

                    if self.No_units > 15:

                        break

                    else:

                        print("You need to enter at least 16 units.")

                else:

                    self.mark = self.prompt_mark(self.unit_code)

                    self.units.append({"unit": self.unit_code , "mark": self.mark})  # Add the unit to the list

                    self.No_units += 1
        
        return self.units

    def count_repeating_units(self):

        unit_counts = Counter(failed_units["unit"] for failed_units in self.units)

        for unit, count in unit_counts.items():

            if count > 3:

                print(f"unit '{unit}' repeats {count} times.")

                return "Not eligible for Honors"
            
            else:
                
                return "for further assessment"


    def get_OUST_status(self):

        return self.is_OUST_student



