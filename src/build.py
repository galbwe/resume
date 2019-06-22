from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
font_config = FontConfiguration()
html = HTML(filename='./resume.html')
css = CSS(filename='./resume.css', font_config=font_config)
html.write_pdf('./build/resume.pdf', stylesheets=[css], font_config=font_config)
