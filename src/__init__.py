#!/usr/bin/env python
import os
from create_post import *

class Sighter(object):
    def run(self):
        print("Hello, world!")

    def markdown_html_driver(self):
            markdown_output = Post().read_markdown_file('../tests/2022-01-01-test_post.md')
            html_output = Post().markdown_to_html(markdown_output)
            Post().create_post(html_output, '../themes/post.html', '../output/blog/new_post.html')

    # Create post with template and add html

if __name__ == '__main__':
    Sighter().markdown_html_driver() 
