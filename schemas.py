from graphene import Int, Boolean, String, Date, ObjectType


class CourseType(ObjectType):
    id = Int(required=True)
    title = String(required=True)
    mentor = String()
    active = Boolean()
    create_date = Date()
