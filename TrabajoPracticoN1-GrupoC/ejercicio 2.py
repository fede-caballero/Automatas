import re

class ReadLine:
    def __init__(self, text):
        self.text = text

    def read_txt_lines(self):
        lines_prueba = []
        lines = []
        file = open(self.text, "r")
        for i in file:
            lines_prueba.append(i)
        for i in lines_prueba:
            if "\n" in i:
                variable = i.replace("\n", "")
                lines.append(variable)
        return lines

example_text = ReadLine(
    "./Archivos_Texto/urls.txt")
urls = example_text.read_txt_lines()

def analizer(url):
    pattern = re.compile("(^https?://)|(www)?[\w]+(\.[\w]+\-{1}[\w]+)+[/#?]?.*$")
    
    if pattern.match(url):
        print(f'The string \033[32m{urls[count]}\033[0m contains the pattern')
    else:
        print(f'The string \033[32m{urls[count]}\033[0m does not contain the pattern')

count = 0
for i in urls:
    analizer(urls[count])
    count += 1
