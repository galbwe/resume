from functools import partial
import json
import os
import sys

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


def get_template(resume, html_path='./html'):
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
    return template

def get_weasyprint_html(template):
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


def build_pdf(config='config.json', build='./build/resume.pdf'):
    font_config = FontConfiguration()
    resume = parse_config(config)
    html = get_html(resume)
    stylesheets = get_stylesheets(font_config)
    html.write_pdf(build, stylesheets=stylesheets, font_config=font_config)


def get_css_filenames(css_dir='./css'):
    filenames = []
    for filename in os.listdir(css_dir):
        if filename.split('.')[-1] == 'css':
            filenames.append(filename)
    return filenames


def create_link(filename):
    return f'<link rel="stylesheet" href="../css/{filename}">'


def build_html(config='config.json', build='./build/resume.html'):
    resume = parse_config(config)
    template = get_template(resume)
    # get links to css
    _, _, filenames = next(os.walk('./css'))
    filenames = [f for f in filenames if f.endswith('.css')]
    links = [create_link(filename) for filename in filenames]
    body = template.render(resume=resume)
    html = '''
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
     <head>
      <meta charset="utf-8">
      {links}
      <title>Resume</title>
     </head>
      {body}

    </html>
    '''.format(links='\n'.join(links), body=body)
    with open(build, 'w') as f:
        f.write(html)

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'pdf':
        build_pdf()
    elif mode == 'html':
        build_html()
    else:
        print('Yo! You need to specify a development mode!')
