import os

from jinja2 import Environment, FunctionLoader, select_autoescape

class Component:
    def __init__(self, template):

        self.template = template

        html_path = os.path.abspath(os.path.dirname(__file__))
        html_path = os.path.join(html_path, os.path.pardir, 'html')
        html_path = os.path.abspath(html_path)
        self.html_path = html_path

        def load_template(name):
            if name in (f for f in os.listdir(html_path)):
                return open(os.path.join(html_path, name)).read()
            return None

        env = Environment(
            loader=FunctionLoader(load_template),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.env = env

    def render(self):
        template = self.env.get_template(self.template)
        return template.render(**self.params)
