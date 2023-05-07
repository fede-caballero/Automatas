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
    "./Archivos_Texto/direcciones.txt")
dir_ip = example_text.read_txt_lines()


def analizer(dirs):
    if re.fullmatch("^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", dirs):
        print(f'The IP address: {dir_ip[count]} is valid')

    else:
        print(f'The IP address: {dir_ip[count]} is not valid')


count = 0
for i in dir_ip:
    analizer(dir_ip[count])
    count += 1