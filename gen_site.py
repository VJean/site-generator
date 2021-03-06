#!/bin/env python3

import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = '%s/templates/' % base_dir
target_dir = "/home/jean/git/vjean.github.io"

env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True, lstrip_blocks=True
)

site_local = True

# sortir dans le bon dossier : /home/jean/git/vjean.github.io/

for f in ["index.html", "parcours.html", "projets.html"]:
    template = env.get_template(f)
    target_file = os.path.join(target_dir, f)
    with open(target_file, "w") as fileout:
        fileout.write(template.render(site_local=site_local))
        print("wrote", target_file)

for f in ["index_en.html", "parcours_en.html", "projets_en.html"]:
    template = env.get_template(f)
    target_file = os.path.join(target_dir, "en", f.replace('_en', ''))
    with open(target_file, "w") as fileout:
        fileout.write(template.render(site_local=site_local))
        print("wrote", target_file)
