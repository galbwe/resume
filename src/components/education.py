from .component import Component

class EducationSection(Component):
    def __init__(self, template, degrees):
        super().__init__(template)
        self.params = {
            "degrees": degrees
        }

class Degree(Component):
    def __init__(self, template, degree, school, gpa, graduation_date):
        super().__init__(template)
        self.params = {
            "degree": degree,
            "school": school,
            "gpa": gpa,
            "graduation_date": graduation_date
        }
