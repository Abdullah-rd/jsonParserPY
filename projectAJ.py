import re
import os
import json

TOKEN_TYPES = {
    "LBRACE": r"\{",
    "RBRACE": r"\}",
    "LBRACKET": r"\[",
    "RBRACKET": r"\]",
    "COLON": r":",
    "COMMA": r",",
    "STRING": r'"(?:\\.|[^\\"])*"',
    "NUMBER": r"\d+(\.\d+)?",
    "TRUE": r"true",
    "FALSE": r"false",
    "NULL": r"null",
}



def tokenize(jsonString):
    jsonString = jsonString.strip()
    print("Votre contenu JSON : ", jsonString)
    tokens = []

    while jsonString:
        for token_type, pattern in TOKEN_TYPES.items():
            match = re.match(pattern, jsonString)
            if match:
                token_value = match.group()
                tokens.append((token_type, token_value))
                jsonString = jsonString[len(token_value) :].strip()
                break
    #print(tokens)
    return tokens


def parserTOKENS(tokens):
    def parse_object():
        obj = {}
        token = tokens.pop(0)
        
        if token[0] == "RBRACE":
            return obj

        while True:
            key = token[1][1:-1]
            token = tokens.pop(0)
            value = parse_value()
            obj[key] = value
            token = tokens.pop(0)

            if token[0] == "RBRACE":
                break
            elif token[0] == "COMMA":
                token = tokens.pop(0)

        return obj

    def parse_array():

        arr = []
        token = tokens[0]
        if token[0] == "RBRACKET":
            return arr
        while True:
            value = parse_value()
            arr.append(value)
            token = tokens.pop(0)
            if token[0] == "RBRACKET":
                break
        return arr



    def parse_value():
        token = tokens.pop(0)
        if token[0] == "LBRACE":
            return parse_object()
        elif token[0] == "LBRACKET":
            return parse_array()
        elif token[0] == "STRING":
            return token[1][1:-1]
        elif token[0] == "NUMBER":
            return float(token[1]) if "." in token[1] else int(token[1])
        elif token[0] == "TRUE":
            return True
        elif token[0] == "FALSE":
            return False
        elif token[0] == "NULL":
            return None
    value = parse_value()
    return value

# cette fonction est comme un pont entre la tokenisation et parsing

def parserJSON(jsonString):
    tokens = tokenize(jsonString)
    return parserTOKENS(tokens)


 # cette fonction valide la chaîne JSON et retourne True si elle est bien formée, False sinon.

def validerJSON(jsonString):
    try:
        json.loads(jsonString)
        return True
    except ValueError as e:
        print(f"Erreur de validation : {e}")
        return False




# cette fonction lit le fichier json et enregistre sa valeur String dans jsonString

def lireJSON(file_path):
    try:
        with open(file_path, "r") as file:
            jsonString = file.read().strip()
        return jsonString
    except FileNotFoundError:
        print(f"Erreur : fichier '{file_path}' non trouvé.")
    except Exception as e:
        print(f"Erreur : {e}")


#function main
def main():
    dossier_Exemples = "examples"
    if not os.path.exists(dossier_Exemples):
        print(f"Erreur : répertoire '{dossier_Exemples}' non trouvé.")
        return

    print("Fichiers disponibles dans le dossier 'examples' :")
    Fdispo = os.listdir(dossier_Exemples)
    for i, file_name in enumerate(Fdispo, start=1):
        print(f"{i}. {file_name}")

    try:
        file_index = int(input("Entrez le numéro du fichier : ")) - 1
        if 0 <= file_index < len(Fdispo):
            file_name = Fdispo[file_index]
        else:
            print("Numéro de fichier invalide.")
            return
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return

    file_path = os.path.join(dossier_Exemples, file_name)
    jsonString = lireJSON(file_path)

    if not jsonString:
        return

    is_valid = validerJSON(jsonString)
    print(f"La chaîne JSON est-elle valide ? {is_valid}")

    if is_valid:
        res = parserJSON(jsonString)
        print('La nouvelle structure de données est enregistrée en "res" : ')
        print(res)

if __name__ == "__main__":
    main()

