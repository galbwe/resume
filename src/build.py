from functools import partial
import os

from jinja2 import Environment, FunctionLoader, select_autoescape
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration


font_config = FontConfiguration()

def load_template(name, html_path='./html'):
    if name in (f for f in os.listdir(html_path)):
        return open(os.path.join(html_path, name)).read()
    return None

# jinja2 environment
env = Environment(
    loader=FunctionLoader(partial(load_template, html_path='./html')),
    autoescape=select_autoescape(['html', 'xml'])
)

# render jinja2 template
template = env.get_template('resume.html')
html = HTML(string=template.render(subtitle='Software Developer'))

# css stylesheets
stylesheets = []
css_path = './css'
for f in os.listdir(css_path):
    filename = os.path.join(css_path, f)
    if os.path.isfile(filename):
        css = CSS(filename=filename, font_config=font_config)
        stylesheets.append(css)

html.write_pdf('./build/resume.pdf', stylesheets=stylesheets,
               font_config=font_config)
