import requests
from bs4 import BeautifulSoup

URL = 'https://www.therecipedepository.com/'
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="content")
# print("ID results: ", id_results.prettify())

job_elements = results.find_all("div", class_="recipe")

# counter = 0
for job_element in job_elements:
    # counter += 1
    #print("element ", counter, " : ",  job_element, end="\n"*2)
    # title_element = job_element.find("img alt")
    # print(title_element)

    recipe_name = job_element.find("h3", class_="recipe-name")
    recipe_name = recipe_name.text.strip()

    # ingredient = job_element.find("li", class_="ingredients")
    # ingredient = ingredient.text.strip()

    print(recipe_name)
    # print(ingredient)
