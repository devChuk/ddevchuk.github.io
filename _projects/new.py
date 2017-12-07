#Just a simple script to automate the YAML front matter in new posts
import datetime
import os

title = raw_input('\nEnter title: ')
fileName= title.replace(" ", "_").lower() + '.md'
print fileName + '\n'

text = """---
layout: project
title: Parrot
date: Feb 2015
thumbnail: http://devchuk.github.io/devchukV1/res/img/portimg/parrot/prof.jpg
thumbnail_size: half-img
client: HACKATHON
client_name: McHacks II
role: Full-stack developer
platforms: Android, iOS, Android Wear
status: Dormant
featured: True
desc: Here is a medium-length description about the project.
---
"""

file = open(fileName, "w")
file.write(text)

print '\nFile is generated!'

os.system("sublime-text " + fileName)
