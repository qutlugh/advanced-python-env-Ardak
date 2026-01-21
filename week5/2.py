import json

def process_student_grades(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)

        updated_data = []
        for student in data:
            grades = student['grades']
            avg_grade = sum(grades) / len(grades) if grades else 0
            
            new_student = student.copy()
            new_student['average_grade'] = round(avg_grade, 2)
            updated_data.append(new_student)

        with open(output_file, 'w') as f:
            json.dump(updated_data, f, indent=4)
            
        print(f"Task 2 Complete. Updated data saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")

process_student_grades("students.json", "students_analyzed.json")