def calculate_grade(marks: int) -> dict:
    """
    Returns grade, grading point, and remark based on marks.

    :param marks: Marks obtained by the student (0-100)
    :return: Dictionary containing grade, grading point, and remark
    """
    if marks < 0 or marks > 100:
        return {"error": "Invalid marks. Please enter a value between 0 and 100."}

    grades = {}

    if marks >= 91:
        grades.update(
            {"grade": "A1", "grading_point": 10.0, "remark": "Outstanding performance!"}
        )
    elif marks >= 81:
        grades.update(
            {"grade": "A2", "grading_point": 9.0, "remark": "Excellent performance!"}
        )
    elif marks >= 71:
        grades.update(
            {"grade": "B1", "grading_point": 8.0, "remark": "Very good performance"}
        )
    elif marks >= 61:
        grades.update(
            {"grade": "B2", "grading_point": 7.0, "remark": "Good performance"}
        )
    elif marks >= 51:
        grades.update(
            {"grade": "C1", "grading_point": 6.0, "remark": "Fair performance"}
        )
    elif marks >= 41:
        grades.update(
            {"grade": "C2", "grading_point": 5.0, "remark": "Average performance"}
        )
    elif marks >= 33:
        grades.update(
            {
                "grade": "D",
                "grading_point": 4.0,
                "remark": "Below Average / Marginal Pass",
            }
        )
    else:  # marks < 33
        grades.update(
            {"grade": "E2", "grading_point": 0.0, "remark": "Needs Improvement (Fail)"}
        )

    return grades


print(calculate_grade(87))
print(calculate_grade(29))
print(calculate_grade(105))  # Invalid marks
