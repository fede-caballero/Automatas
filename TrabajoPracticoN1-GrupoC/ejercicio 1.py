import re


class read_line:
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


example_text = read_line(
    "./Archivos_Texto/e-mails.txt")
correos = example_text.read_txt_lines()


def analizer(mails):
    if re.fullmatch("[A-Za-z][A-Za-z0-9._-]+[A-Za-z0-9]@[A-Za-z]+\.(com|net)+(\.[A-Za-z]{2})?", mails):
        print(f'La cadena {correos[count]} contiene el patron')

    else:
        print(f'La cadena {correos[count]} no contiene el patron')


count = 0
for i in correos:
    analizer(correos[count])
    count += 1

