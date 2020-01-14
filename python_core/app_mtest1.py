import lmk1parser
import listeObject
import lmk1viewer
PATH = "tests_files/test_file1.lmk"
# Récupération des données de fichier de la liste
parser = lmk1parser.LMK1PARSER(PATH)
liste = parser.parse()
# Affichage de la liste
lmk1viewer.LMK1Viewer.direct_viewer(liste)