from requests import get, post
from yaml import load, FullLoader, dump
from re import findall, search
from bs4 import BeautifulSoup

yaml = get("https://www.w3schools.io/file/yaml-sample-example/")
yaml_tags = BeautifulSoup(yaml.text, "html5lib")

exemplo = yaml_tags.find_all("pre", attrs = {"class" : "chroma"})
exemplos = [pre.text for pre in exemplo]

comentarios = yaml_tags.find_all("span", attrs = {"class" : "c"})
comentarios = [span.text for span in comentarios]
for cada in range(len(comentarios)):
    comentario = " ".join(findall(r"\w+", comentarios[cada]))
    print(comentario)

with open("novo_yaml.yml", "w") as file:
    dump(exemplos, file)

with open("novo_yaml.yml") as file:
    yaml_file = load(file, Loader=FullLoader)
print(yaml_file)
