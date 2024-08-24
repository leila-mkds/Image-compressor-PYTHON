# Importation de la bibliothèque PIL et des fonctions
import PIL
from PIL import Image
from tkinter.filedialog import *

import PIL.Image

file_path=askopenfilename() # Ouvre une boîte de dialogue pour sélectionner un fichier image à ouvrir
img=PIL.Image.open(file_path) # Ouvre l'image sélectionnée et la charge dans l'objet `img`
myHeight,myWidth=img.size # Obtient la hauteur et la largeur de l'image

img=img.resize((myHeight, myWidth), PIL.Image.LANCZOS) # Redimensionne l'image en utilisant l'algorithme de réduction de qualité LANCZOS
save_path=asksaveasfilename() # Ouvre une boîte de dialogue pour sélectionner l'emplacement de sauvegarde
img.save(save_path+"compressed.jpg")  # Sauvegarde l'image redimensionnée avec le nom "compressed.jpg" à l'emplacement choisi