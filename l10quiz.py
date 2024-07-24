## l10quiz.py

def find_max_in_list(numbers):
    if not numbers:
        return None
    max_number = 0
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

