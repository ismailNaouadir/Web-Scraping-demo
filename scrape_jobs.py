import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Look for Python jobs
print("PYTHON JOBS\n==============================\n")
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for index, job_element in enumerate(python_job_elements):
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    with open(f'posts/{index}.txt', 'w') as f:
        f.write(f'Title: {title_element.text.strip()} \n')
        f.write(f'Company: {company_element.text.strip()} \n')
        f.write(f'Location: {location_element.text.strip()} \n')
        link_url = job_element.find_all("a")[1]["href"]
        f.write(f"Apply here: {link_url}\n")
