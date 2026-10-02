
def check_students(student_list, student_cohort):
    for student in student_list:
        if student['cohort'].lower() != student_cohort.lower():
            return False
    return True


# Test false case
print(f'Expected: False, Actual: {check_students([
    {"name": "Ben", "cohort": "October"},
    {"name": "Amanda", "cohort": "April"},
    {"name": "Matt", "cohort": "April"}
  ], 'april')}')

# Test true case
print(f'Expected: True, Actual: {check_students([
    {"name": "Ben", "cohort": "April"},
    {"name": "Amanda", "cohort": "April"},
    {"name": "Matt", "cohort": "April"}
  ], 'april')}')