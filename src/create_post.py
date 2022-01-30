import os
import markdown

class Post(object):
    def run(self):
        print("Hello, post!")

    # Step 1: Read in markdown from posts directory
    def read_markdown_file(self, path):
        with open(path, 'r') as f:
            lines = f.read()
    
        print(lines)
        return lines

    # Step 2: Convert markdown to static HTML
    def markdown_to_html(self,markdown_input):
        html_output = markdown.markdown(markdown_input)
        return html_output

    # TODO
    # Step 3: Append static html into template
    def create_post(self, html_output):
        return html_output






        
