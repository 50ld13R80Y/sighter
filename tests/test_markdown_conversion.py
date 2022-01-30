import markdown

output = markdown.markdown('''
# Step 1
## Step 2
* item 1
* item 2

Visit [the tutorials page](https://www.digitalocean.com/community/tutorials) for more tutorials!
''')

print(output)
