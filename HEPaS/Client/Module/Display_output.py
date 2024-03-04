def print_unit_marks_table(unit_marks):

    # Print table header

    print("| {:<10} | {:<10} |".format("Unit", "Mark"))

    print("|" + "-" * 12 + "|" + "-" * 12 + "|")


    # Print each row of the table
    for entry in unit_marks:

        print("| {:<10} | {:<10} |".format(entry['unit'], entry['mark']))



def print_course_info(course_average, best_8_scores_average, eligibility):

    # Use print statements with line breaks for better readability
    print(f"\nCourse Average: {course_average}\n")
    
    print(f"Best 8 Scores Average: {best_8_scores_average}\n")
    
    print(f"Eligibility: {eligibility}\n")
    