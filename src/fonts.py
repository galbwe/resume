import os
import re

import requests

family_re = re.compile(r"font-family: '([-_A-Za-z0-9]+)'")
style_re = re.compile(r"font-style: ([-_A-Za-z0-9]+)")
weight_re = re.compile(r"font-weight: ([0-9]+)")
display_re = re.compile(r"font-display: ([-_A-Za-z0-9]+)")
local_font_re = re.compile(r"local\('([-_A-Za-z0-9]+)'\)")
src_re = re.compile(r"url\((https:.+\.ttf)\)")


class FontFace:
    def __init__(self, family, style, weight, display, local_font, src):
        self.family = family
        self.style = style
        self.weight = weight
        self.display = display
        self.local_font = local_font
        self.src = src

    def __repr__(self):
        class_name = type(self).__name__
        args = ', '.join(f'{k}={v}' for (k, v) in vars(self).items())
        return f"{class_name}({args})"

    def __str__(self):
        # breakpoint()
        return """
        @font-face {{
            font-family: '{self.family}';
            font-style: {self.style};
            font-weight: {self.weight};
            font-display: {self.display};
            src: local('{self.local_font}');
        }}
        """.format(self=self)

    @classmethod
    def from_name(cls, family, fonts_dir="/root/.fonts"):
        url = f"https://fonts.googleapis.com/css?family={family}&display=swap"
        resp = requests.get(url)
        content = resp.content.decode('utf-8')

        family = family_re.search(content).group(1)
        style = style_re.search(content).group(1)
        weight = weight_re.search(content).group(1)
        display = display_re.search(content).group(1)

        local_font = local_font_re.search(content).group(1)
        local_font = f'{fonts_dir}/{local_font}.ttf'

        src = src_re.search(content).group(1)

        return cls(family, style, weight, display, local_font, src)

    def to_ttf(self):
        resp = requests.get(self.src)
        with open(self.local_font, 'wb') as f:
            f.write(resp.content)


def get_lora(target_dir='/root/.fonts'):
    lora = FontFace.from_name('Lora')
    lora.to_ttf()
    make_fonts_css('Lora')
    print(str(lora))


def make_fonts_css(*font_names, target='./css/fonts.css'):
    css = open(target, 'w')
    for name in font_names:
        font_face = FontFace.from_name(name)
        css.write(str(font_face))
    css.close()


if __name__ == '__main__':
    get_lora()
