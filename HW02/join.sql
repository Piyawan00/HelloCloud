SELECT Student.student_id,Student.f_name,Student.l_name,Registration.Subject_id,Subject_name,grade,Teacher.f_name,Teacher.l_name
FROM Student
JOIN Registration on student.student_id = Registration.student_id
JOIN Subject on Registration.subject_id = Subject.subject_id
JOIN Teacher on Subject.teacher_id = Teacher.teacher_id
