class ServerBasicOperations:
    def __init__(self):
        self.scores = []

    def display_scores(self):

        print("Individual Scores:")

        for score in self.scores:

            print(f"{score['unit']}: {score['mark']}")

    def calculate_course_average(self):

        if not self.scores:

            return None
        
        total_marks = sum(score['mark'] for score in self.scores)

        return total_marks / len(self.scores)

    def calculate_best8_average(self):

        if len(self.scores) < 8:

            return None
        
        sorted_scores = sorted(self.scores, key=lambda x: x['mark'], reverse=True)

        best8_scores = sorted_scores[:8]

        total_best8_marks = sum(score['mark'] for score in best8_scores)

        return total_best8_marks / 8


    def evaluate_eligibility(self):

        if not self.scores:

            return "Not eligible"

        average_mark = self.calculate_course_average()

        best8_average = self.calculate_best8_average()

        fail_count = sum(1 for score in self.scores if score['mark'] < 50)

        if len(self.scores) <= 15:

            return f"{average_mark:.2f}, completed less than 16 units! DOES NOT QUALIFY FOR HONORS STUDY!"

        elif fail_count >= 6:

            return f"{average_mark:.2f}, with 6 or more Fails! DOES NOT QUALIFY FOR HONORS STUDY!"

        elif average_mark >= 70:

            return f"{average_mark:.2f}, QUALIFIES FOR HONOURS STUDY!"

        elif 65 <= average_mark < 70 and best8_average >= 80:

            return f"{average_mark:.2f}, {best8_average:.2f}, QUALIFIES FOR HONOURS STUDY!"

        elif 65 <= average_mark < 70 and best8_average < 80:

            return f"{average_mark:.2f}, {best8_average:.2f}, MAY HAVE GOOD CHANCE! Need further assessment!"

        elif 60 <= average_mark < 65 and best8_average >= 80:

            return f"{average_mark:.2f}, {best8_average:.2f}, QUALIFIES FOR HONOURS STUDY!"

        else:
            
            return f"{average_mark:.2f}, {best8_average:.2f}, Need further assessment!"


    def process_data(self, data):

        # Assuming data is a list of dictionaries with keys 'unit' and 'mark'
        self.scores = [{'unit': entry['unit'], 'mark': entry['mark']} for entry in data]

    def send_evaluation_result(self):

        eligibility_result = self.evaluate_eligibility()

        return eligibility_result




