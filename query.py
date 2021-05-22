import json

from graphene import ObjectType, List, Mutation, Field, String, Int

from schemas import CourseType


class QueryCourse(ObjectType):
    course_list = None
    get_course = List(CourseType)
    
    def resolve_get_course(self, info):
        with open("./courses.json") as courses:
            course_list = json.load(courses)
        return course_list


class CourseCreator(Mutation):
    course = Field(CourseType)

    class Arguments:
        id = Int(required=True)
        title = String(required=True)
        
    def mutate(self, info, id, title):
        with open("./courses.json", "r+") as courses:
            course_list = json.load(courses)
            course_list.append({"id": id, "title": title})
            courses.seek(0)
            json.dump(course_list, courses, indent=2)
        return CourseCreator(course=course_list[-1])


class Mutation(ObjectType):
    create_course = CourseCreator.Field()
