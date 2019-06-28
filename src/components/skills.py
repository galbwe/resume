from .component import Component

class Skills(Component):
    def __init__(self, template, skills):
        super().__init__(template)
        self.params = {
            'skills': skills
        }
