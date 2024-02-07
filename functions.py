from models import Teachers, Classes


def insert_new_teacher(name: str, last_name: str, telephone: str, email: str):
    new_teacher = Teachers(
        name=name, last_name=last_name, telephone=telephone, email=email
    )
    new_teacher.save()


def delete_teacher(email: str):
    Teachers.delete().where(Teachers.email == email).execute()


def get_all_teachers():
    for teacher in Teachers.select():
        print(
            "Name: {} - Last Name: {} - Telephone: {} - Email: {}".format(
                teacher.name, teacher.last_name, teacher.telephone, teacher.email
            )
        )


def insert_new_class(
    code_class, start_date_course, end_date_course, schedule, teacher_id
):
    new_class = Classes(
        code_class=code_class,
        start_date_course=start_date_course,
        end_date_course=end_date_course,
        schedule=schedule,
        teacher_id=teacher_id,
    )
    new_class.save()


def get_all_classes():
    query = (
        Teachers.select(Teachers, Classes)
        .join(Classes)
        .group_by(Classes.code_class)
        .where(Teachers.teacher_id == Classes.teacher_id)
    )

    for course in query:
        print(
            "The course {} starts on {} and finishes on {}, the teacher will be {} {}".format(
                course.classes.code_class,
                course.classes.start_date_course,
                course.classes.end_date_course,
                course.name,
                course.last_name,
            )
        )
