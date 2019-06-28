from .component import Component

class ExperienceSection(Component):
    def __init__(self, template, jobs):
        super().__init__(template)
        self.params = {
            "jobs": jobs
        }

class Job(Component):
    def __init__(self, template, title, location, company, start_date, end_date,
                details):
        super().__init__(template)
        self.params = {
            "title": title,
            "location": location,
            "company": company,
            "start_date": start_date,
            "end_date": end_date,
            "details": details
        }
