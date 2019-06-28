from .component import Component

class AwardsSection(Component):
    def __init__(self, template, awards):
        super().__init__(template)
        self.params = {
            "awards": awards
        }
        
class Award(Component):
    def __init__(self, template, award, year):
        super().__init__(template)
        self.params = {
            "award": award,
            "year": year
        }
