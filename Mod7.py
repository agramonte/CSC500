def main():
    #Dictionary with room numbers.
    rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    #Dictionary with location.
    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    #Dictionary with meeting times.
    meetingTimes = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    print("Welcome to the Course Information Program!")

    # Display available courses
    print(f"Available courses: {', '.join(rooms.keys())}")

    while True:
        # Prompt user for course number
        # .strip().upper() handles extra spaces and lowercase input
        courseNumber = input("\nEnter a course number (or 'q' to quit, or 'l' to list all courses details): ").strip().upper()

        if courseNumber == 'Q':
            print("Goodbye!")
            break
        elif courseNumber == 'L':
            for course in rooms.keys():
                print(f"Course: {course}")
                print(f"Room Number: {rooms[course]}")
                print(f"Instructor: {instructors[course]}")
                print(f"Meeting Time: {meetingTimes[course]}")
                print("-" * 25)
            continue

        #check if course number exists in the rooms
        if courseNumber in rooms:
            print(f"Room Number: {rooms[courseNumber]}")
            print(f"Instructor: {instructors[courseNumber]}")
            print(f"Meeting Time: {meetingTimes[courseNumber]}")
        else:
            print("Course number not found.")

if __name__ == "__main__":
    #runs the program
    main()