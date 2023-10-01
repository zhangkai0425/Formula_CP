# Copy formulas in Latex format from any website and save them in a markdown file.
import requests
from bs4 import BeautifulSoup
import re

# Input URL
url = input("Please input URL:")

# Send HTTP requests to get web content
response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    html_content = response.text
else:
    print("Unable to get web content")
    exit()

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Use regular expressions to match formulas in tex format that contain "="
tex_formulas = re.findall(r'data-tex="(.*?)"', str(soup))

# Write the matching formula to the Markdown file
cnt = 0
with open('formula.md', 'w', encoding='utf-8') as file:
    for formula in tex_formulas:
        if '=' in formula:
            cnt += 1
            file.write(f"$$\n{formula}\n$$\n\n")
print(f"{cnt} formulas with '=' saved to formula.md")
