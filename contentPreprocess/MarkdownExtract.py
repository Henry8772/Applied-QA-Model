import sys
import re

import markdown
from bs4 import BeautifulSoup

# sys.stdin.reconfigure(encoding='utf-8')
# sys.stdout.reconfigure(encoding='utf-8')

class MarkdownExtract:
    def __init__(self, file_path=None):
        self.n = 0
        self.file_path = file_path or "assets/raa_notes.md"

    def read(self):
        f = open(self.file_path, 'r', encoding='utf-8')
        htmlmarkdown = markdown.markdown(f.read())
        processed = self.preprocess(htmlmarkdown)
        list = processed.split("<h4>")[1:]
        all_content = []
        for i in list:
            paragraph = i.split("</h4>")
            content = {'title': paragraph[0], 'content': paragraph[1]}
            all_content.append(content)
        print(all_content)

    def preprocess(self, content):
        replaceDict = {r"<h[1-3]>.*</h[1-3]>": "", r'(\n+)': ''}

        # r'(\n+)': ':',
        for k, v in replaceDict.items():
            content = re.sub(k, v, content)
        return content



mk = MarkdownExtract()
mk.read()


# step 1. Read markdown notes
# Step 2. Calculate each h2 titles cosine similarity with the question
# step 3. for each content, apply bert model to obtain the optimal accuracy score
