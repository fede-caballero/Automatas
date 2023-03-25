print("String Validation")
string_1 = str(input("Enter your string: "))


def validate_string(string):
    # Comprueba si el string contiene al menos un carácter alfanumérico.
    alphanum = any(i.isalnum() for i in string)

    # Comprueba si el string contiene al menos una letra.
    letter = any(i.isalpha() for i in string)

    # Comprueba si el string contiene al menos una letra mayúscula.
    supper = any(i.isupper() for i in string)

    # Comprueba si el string contiene al menos una letra minúscula.
    lower = any(i.islower() for i in string)

    # Comprueba si el string contiene al menos un dígito.
    digit = any(i.isdigit() for i in string)

    # Comprueba si el string contiene al menos 8 caracteres.
    string_len = len(string) >= 8

    return alphanum, letter, supper, lower, digit, string_len


print(validate_string(string_1))            
