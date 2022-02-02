import os
import markdown
from bs4 import BeautifulSoup

class Post(object):

    BLOG_TEMPLATE_PATH = '../themes/post.html'

    def run(self):
        print("Hello, post!")

    # Step 1: Read in markdown from posts directory
    def read_markdown_file(self, path):
        with open(path, 'r') as f:
            lines = f.read()
    
        #print(lines)
        return lines

    # Step 2: Convert markdown to static HTML
    def markdown_to_html(self,markdown_input):
        html_output = markdown.markdown(markdown_input)
        return html_output

    # Open Blog Template
    # Step 3: Append static html into template
    def create_post(self, html_output, file_path_of_template, parsed_post):

        # the converted markdown
        # = open(html_output, "r").read()

        # the blog template
        y = open(file_path_of_template, "r")
        blog_template = y.read()

        # rename blog remplate
        updated_html_page = blog_template.replace("REPLACE ME", html_output)
        
        soup = BeautifulSoup(updated_html_page, "html.parser")
        print(soup.prettify())
        
        file = open(parsed_post, "w+")
        
        file.write(soup.prettify())
        

    '''
    Idea have 7 unique tags in the tamplate:
    For the blog index replace the 7 tags with the 7 newest blogs
    '''





        
