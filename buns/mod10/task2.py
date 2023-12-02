import re
import requests

page = requests.get('http://www.columbia.edu/~fdc/sample.html')

pattern = re.compile(r'<h3\b[^>]*>(.*?)</h3>', re.IGNORECASE | re.DOTALL)
print(pattern.findall(page.text))
