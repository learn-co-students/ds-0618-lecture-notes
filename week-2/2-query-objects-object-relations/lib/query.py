class Query:
    @classmethod
    def find_by_name(cls, otherClass, name):
        return [object for object in otherClass.all() if object.name == name]
