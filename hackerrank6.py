def sorted_students(names_scores):
    # Extract all scores
    scores = [student[1] for student in names_scores]

    # Find the unique scores and sort them
    sorted_scores = sorted(set(scores))

    # Check if there are at least two different scores
    if len(sorted_scores) < 2:
        print("Not enough unique scores.")
        return

    # Get the second lowest score
    second_lowest = sorted_scores[1]

    # Find names of students with the second lowest score
    names_second_lowest = [student[0] for student in names_scores if student[1] == second_lowest]

    # Sort the names alphabetically
    names_second_lowest.sort()

    # Print each name on a new line
    for name in names_second_lowest:
        print(name)


if __name__ == '__main__':
    names_scores = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        names_scores.append([name, score])

    sorted_students(names_scores)
