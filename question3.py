def calculate_average(scores):
    """Calculates and returns the average of a list of scores."""
    return sum(scores) / len(scores)

def get_letter_grade(average):
    """Returns the letter grade based on the average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    scores = []

    # Ask how many test scores to enter
    while True:
        try:
            count = int(input("How many test scores would you like to enter? "))
            if count <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            # ValueError is a bad input
            print("Invalid input. Please enter a number.")

    # Collect each score
    i = 0
    # i is a common loop counter variable. 
    # In this context, it stands for the index or iteration number of how many test scores have been entered so far.  
    while i < count:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                i += 1
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input, please enter a number.")

    # Calculate average and get letter grade
    average = calculate_average(scores)
    letter_grade = get_letter_grade(average)

    # Display the results
    print(f"\nAverage Score: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")

# Run the program
main()
        