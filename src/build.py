from datetime import datetime
import os

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

BUILD_DIR = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    os.path.pardir,
    'build'
)

date = datetime.now().strftime('%m-%d-%Y_%H-%M')
target_filename = f'wes-galbraith-resume_{date}.pdf'

target = os.path.join(BUILD_DIR, target_filename)

font_config = FontConfiguration()
html = HTML(filename='wes-galbraith-resume.html')
css = CSS(filename='wes-galbraith-resume.css')

html.write_pdf(target, stylesheets=[css], font_config=font_config)
