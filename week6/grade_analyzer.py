# Week 6 - Exercise 2
# Student Grade Analyzer

student_records = []

print("=== Student Grade Analyzer ===")

# Collect 6 students
for i in range(1, 7):
    name = input(f"\nStudent {i} name: ")
    score = int(input("Score: "))
    student_records.append((name, score))


# Extract scores
scores = [score for name, score in student_records]

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

unique_scores = set(scores)

# Grade distribution
grade_distribution = {}
for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1


# Display results
print("\n=== RESULTS ===")

print("\nStudent Records:")
for name, score in student_records:
    print(f"{name}: {score}")

print(f"\nHighest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Average Score: {average:.2f}")

print("\nUnique Scores:")
print(unique_scores)

print("\nGrade Distribution:")
for score, count in grade_distribution.items():
    print(f"Score {score}: {count} student(s)")