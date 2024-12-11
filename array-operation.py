def compute_average(marks):
    total, count = 0, 0
    for mark in marks:
        if mark !=-1:
            total += mark
            count += 1
    return total/count if count > 0 else 0

def find_highest_lowest(marks):
    highest, lowest = float('-inf'), float('inf')
    for mark in marks:
        if mark !=-1:
            if mark > highest:
                highest= mark
            if mark < lowest:
                lowest = mark
    return highest, lowest

def count_absent(marks):
    absent_count = 0
    for mark in marks:
        if mark == -1:
            absent_count += 1
    return absent_count

def highest_frequency_mark(marks):
    freq = dict()
    for mark in marks:
        if mark != -1:
            if mark not in freq:
                freq[mark] = 1
            else:
                freq[mark] +=1
    max_freq = 0
    most_frequent = None
    for mark, count in freq.items():
        if count > max_freq:
            max_freq = count
            most_frequent = mark
    return most_frequent

def passed_failed_percentages(marks, passing_score):
    passed, failed, total_students = 0,0,0
    for mark in marks:
        if mark != -1:
            total_students += 1
            if mark >= passing_score:
                passed += 1
            else:
                failed += 1
    passed_percentage = (passed / total_students) * 100 if total_students > 0 else 0
    failed_percentage = (failed / total_students) * 100 if total_students > 0 else 0
    return passed_percentage, failed_percentage

def top_three_scores(marks):
    filtered_marks = [mark for mark in marks if mark != -1]
    for i in range(len(filtered_marks) - 1):
        for j in range(len(filtered_marks) - i - 1):
            if filtered_marks[j] < filtered_marks[j+1]:
                filtered_marks[j], filtered_marks[j + 1] = filtered_marks[j + 1], filtered_marks[j]
    return filtered_marks[:3]

def main():
    marks = [56, 78, 45, -1, 89, 90, 23, 78, -1, 65]  # Example marks list
    passing_score = 40

    print("Average score:", compute_average(marks))
    highest, lowest = find_highest_lowest(marks)
    print("Highest score:", highest)
    print("Lowest score:", lowest)
    print("Number of absent students:", count_absent(marks))
    print("Mark with highest frequency:", highest_frequency_mark(marks))
    pass_percentage, fail_percentage = passed_failed_percentages(marks, passing_score)
    print("Pass percentage:", pass_percentage)
    print("Fail percentage:", fail_percentage)
    print("Top three scores:", top_three_scores(marks))

main()