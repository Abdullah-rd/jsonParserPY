Réalisé par : 
Bendahmane Abderrahmane & Benainouna Redouane Abdallah.
                         
                         Projet DSS :
Sujet 8: Valider et parser un fichier JSON en python .

Groupe : 01.

Explication sur le programme développé :
1.	Validation JSON : La fonction validerJSON prend une chaîne JSON en entrée et tente de la charger en utilisant json.loads. Si la chaîne est valide, elle retourne True, sinon elle retourne False.
2.	Tokenization : La fonction tokenize prend une chaîne JSON en entrée et la découpe en "jetons" (unités lexicales) en utilisant des expressions régulières définies dans le dictionnaire jeton_TYPES. Chaque jeton est une paire (type de jeton, valeur du jeton (Elle utilise le module re pour les expressions régulières)).
3.	Parsing des jetons :La fonction parserJetons prend les jetons générés par la fonction tokenize et les interprète pour construire la structure de données correspondante en Python.Les fonctions parse_object, parse_tab, et parse_value sont utilisées pour parser respectivement les objets JSON, les tableaux JSON, et les valeurs JSON individuelles.
4.	Lecture de fichier JSON : La fonction lireJSON prend un chemin de fichier en entrée, lit le contenu du fichier, et retourne la chaîne JSON.
5.	Main : La fonction main est le point d'entrée du programme. Elle recherche les fichiers JSON dans un répertoire spécifié (exemples) et permet à l'utilisateur de choisir un fichier à traiter. Elle lit le contenu du fichier, valide la chaîne JSON, et si elle est valide, la parse en une structure de données Python. Elle affiche le résultat de la validation et la structure de données Python résultante.
Comment utiliser le programme ?
1.	Assurez-vous d'avoir des fichiers JSON dans le répertoire "exemples", Le script s'attend à trouver des fichiers JSON dans ce répertoire pour les parser.
2.	Après avoir exécuté le script, il affichera la liste des fichiers disponibles dans le répertoire "exemples", entrez le numéro correspondant au fichier que vous souhaitez traiter.
3.	Le script tentera de lire et de valider le fichier JSON sélectionné. (Il vérifie si la syntaxe JSON est valide. Si le JSON est valide, il procède au parsing. sinon, il affiche un message d'erreur.)
4.	Si le JSON est valide, le script le parse en une structure de données Python. La structure de données persée est imprimée, fournissant un aperçu du contenu et de la structure du JSON.
5.	Accéder aux données Passées Depuis que la structure des données imprimées en Python est très similaire à JSON, vous ne remarquerez pas beaucoup de différences. C'est pourquoi, après le parsing, vous pouvez accéder à des éléments spécifiques de données dans la nouvelle structure. Des exemples d'accès aux éléments de données sont inclus sous forme de commentaires dans le script. Vous pouvez les décommenter (Enlever à un endroit d’un programme les signes indiquant un commentaire pour exécuter à nouveau)et les modifier selon vos besoins (Les valeurs passées sont enregistrées dans la variable "res").
Explication sur le format Json :
Json qui veut dire JavaScript Object Notation en français Notation objet issue de JavaScript est un format léger et lisible d’échange de données, il gagne beaucoup en popularité car il est très accessible pour l’homme et la machine, il nécessite moins de code et rend les processus plus rapide.
Références:
https://www.w3schools.com/Python/python_json.asp

https://www.guru99.com/python-regular-expressions-complete-tutorial.html

https://www.geeksforgeeks.org/os-module-python-examples/

https://www.json.org/json-fr.html 

https://notes.eatonphil.com/writing-a-simple-json-parser.html

FIN
