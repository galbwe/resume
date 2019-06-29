from functools import partial
import json
import os

from jinja2 import Environment, FunctionLoader, select_autoescape
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from components.head import Head
from components.resume import Resume
from components.experience import ExperienceSection, Job
from components.skills import Skills
from components.projects import ProjectsSection, Project
from components.awards import AwardsSection
from components.education import EducationSection, Degree
from components.awards import Award, AwardsSection

import fonts

# parse config file
def parse_config(file="config.json"):
    with open(file, 'r') as f:
        config = json.loads(f.read())

    resume = config.get('resume')
    head = resume.get('head')
    head = Head('head.html', **head)
    experience = resume.get('work experience')
    experience = ExperienceSection(
        'experience.html',
        [Job('job.html', **job) for job in experience]
    )
    skills = resume.get('skills')
    skills = Skills('skills.html', skills)

    projects = resume.get('Volunteer Projects')
    projects = ProjectsSection(
        'projects_section.html',
        [Project('project.html', **project) for project in projects]
    )

    education = resume.get('Education')
    education = EducationSection(
        'education.html',
        [Degree('degree.html', **degree) for degree in education]
    )

    awards = resume.get('awards')
    awards = AwardsSection(
        'awards_section.html',
        [Award('award.html', **award) for award in awards]
    )

    return Resume(head, experience, skills, projects, education, awards)


def get_html(resume, html_path='./html'):

    def load_template(name):
        if name in (f for f in os.listdir(html_path)):
            return open(os.path.join(html_path, name)).read()
        return None

    # jinja2 environment
    env = Environment(
        loader=FunctionLoader(load_template),
        autoescape=select_autoescape(['html', 'xml'])
    )

    # render jinja2 template
    template = env.get_template('resume.html')
    return HTML(string=template.render(resume=resume))


# css stylesheets
def get_stylesheets(font_config, css_path='./css'):
    stylesheets = []
    for f in os.listdir(css_path):
        filename = os.path.join(css_path, f)
        if os.path.isfile(filename):
            css = CSS(filename=filename, font_config=font_config)
            stylesheets.append(css)
    return stylesheets


def main(config='config.json', build='./build/resume.pdf'):
    font_config = FontConfiguration()
    resume = parse_config(config)
    html = get_html(resume)
    stylesheets = get_stylesheets(font_config)
    html.write_pdf(build, stylesheets=stylesheets, font_config=font_config)

if __name__ == '__main__':
    main()
