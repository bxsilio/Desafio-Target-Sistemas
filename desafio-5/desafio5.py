def inverter_string(s):
    s_invertida = ''
    for caractere in s:
        s_invertida = caractere + s_invertida
    return s_invertida

# Solicitar a string ao usuário
string_entrada = input("Digite uma string: ")

# Inverter a string
string_invertida = inverter_string(string_entrada)

# Exibir a string invertida
print(f"String invertida: {string_invertida}")
