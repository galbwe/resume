from .component import Component

class ProjectsSection(Component):
    def __init__(self, template, projects):
        super()__init__(template)
        self.params = {
            "Volunteer Projects": projects
        }

class Project(Component):
    def __init__(self, template, organization, project, tech_stack, github_repositories,
                location, start_date, end_date, detail):
        super()__init__(template)
        self.params = {
            "template": template,
            "organization": organization,
            "project": project,
            "tech_stack": tech_stack,
            "github_repositories": github_repositories,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "detail": detail
        }
