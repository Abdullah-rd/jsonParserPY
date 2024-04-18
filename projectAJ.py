import re
import os
import json


jeton_TYPES = {
    "LACCOLADE": "\{", # Le backslash \ dans les expressions régulières est utilisé pour échapper les caractères ayant une signification spéciale, les traitant ainsi littéralement.
    "RACCOLADE": "\}",
    "LCROCHET": "\[",
    "RCROCHET": "\]",
    "COLON": ":",
    "COMMA": ",",
    "STRING": '"[^"]*"', # Cette expression régulière correspond à une chaîne de caractères entourée de guillemets doubles, qui peut contenir n'importe quel caractère SAUF des guillemets doubles.
    "NUMBER": "-?\d+(\.\d+)?",  # Cette expression régulière permet de trouver des valeurs numériques, incluant les entiers et les décimaux, avec un signe négatif et un point décimal optionnels.
    "TRUE": "true",
    "FALSE": "false",
    "NULL": "null",
}




def tokenize(JsonString):
    JsonString = JsonString.strip()
    print("Votre contenu JSON : ", JsonString)
    jetons = []

    while JsonString:
        for jeton_type, pattern in jeton_TYPES.items():
            match = re.match(pattern, JsonString)
            if match:
                jeton_value = match.group()
                jetons.append((jeton_type, jeton_value))
                JsonString = JsonString[len(jeton_value) :].strip()
                break
    #print(jetons)
    return jetons


def parserjetonS(jetons):
    def parse_object():
        obj = {}
        jeton = jetons.pop(0)
        
        if jeton[0] == "RACCOLADE":
            return obj

        while True:
            cle = jeton[1][1:-1]
            jeton = jetons.pop(0)
            value = parse_value()
            obj[cle] = value
            jeton = jetons.pop(0)

            if jeton[0] == "RACCOLADE":
                break
            elif jeton[0] == "COMMA":
                jeton = jetons.pop(0)

        return obj

    def parse_array():

        arr = []
        jeton = jetons[0]
        if jeton[0] == "RCROCHET":
            return arr
        while True:
            value = parse_value()
            arr.append(value)
            jeton = jetons.pop(0)
            if jeton[0] == "RCROCHET":
                break
        return arr



    def parse_value():
        jeton = jetons.pop(0)
        if jeton[0] == "LACCOLADE":
            return parse_object()
        elif jeton[0] == "LCROCHET":
            return parse_array()
        elif jeton[0] == "STRING":
            return jeton[1][1:-1]
        elif jeton[0] == "NUMBER":
            return float(jeton[1]) if "." in jeton[1] else int(jeton[1])
        elif jeton[0] == "TRUE":
            return True
        elif jeton[0] == "FALSE":
            return False
        elif jeton[0] == "NULL":
            return None
    value = parse_value()
    return value

# cette fonction est comme un pont entre la tokenization et parsing

def parserJSON(JsonString):
    jetons = tokenize(JsonString)
    return parserjetonS(jetons)


 # cette fonction valide la chaîne JSON et retourne True si elle est bien formée, False sinon.

def validerJSON(JsonString):
    try:
        json.loads(JsonString)
        return True
    except ValueError as e:
        print(f"Erreur de validation : {e}")
        return False




# cette fonction lit le fichier Json et enregistre sa valeur String dans JsonString

def lireJSON(file_path):
    try:
        with open(file_path, "r") as file:
            JsonString = file.read().strip()
        return JsonString
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
    JsonString = lireJSON(file_path)

    if not JsonString:
        return

    is_valid = validerJSON(JsonString)
    print(f"La chaîne JSON est-elle valide ? {is_valid}")

    if is_valid:
        res = parserJSON(JsonString)
        print('La nouvelle structure de données est enregistrée en "res" : ')
        print(res)
        
        # example1 test print(res["nom"])
        # example2 test print(res[1])
        # example3 test print(res["employees"][0]["email"])
        
if __name__ == "__main__":
    main()

