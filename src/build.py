from functools import partial
import json
import os

from jinja2 import Environment, FunctionLoader, select_autoescape
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from components.head import Head
from components.resume import Resume
import fonts

# parse config file
def parse_config(file="config.json"):
    with open(file, 'r') as f:
        config = json.loads(f.read())

    resume = config.get('resume')
    head = resume.get('head')
    head = Head('head.html', **head)

    experience = None

    skills = None

    projects = None

    education = None

    awards = None

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
