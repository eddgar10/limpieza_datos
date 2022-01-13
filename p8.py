from os import listdir
from nltk.corpus import stopwords
import string
import re

# load one file
#filename = 'txt_sentoken/neg/cv000_29416.txt'
# open the file as read only
#file = open(filename, 'r')
# read all text
#text = file.read()
# close the file
#file.close()

# ruta del las opniniones
path_positivas = 'txt_sentoken/pos/'
path_negativas = 'txt_sentoken/neg/'

#dirs_positivas = listdir( path_positivas )

# This would print all the files and directories
#for file in dirs_positivas:
#	print (file)

#dirs_negativas = listdir(path_negativas )

#for file in dirs_negativas:
#	print (file)
def clean_doc(doc):
	#f = open('positivas_limpias.txt', 'w')
	# split into tokens by white space
	tokens = doc.split()
	# prepare regex for char filtering
	re_punc = re.compile('%s' % re.escape(string.punctuation))
	# remove punctuation from each word
	tokens = [re_punc.sub(" ", w) for w in tokens]
	# remove remaining tokens that are not alphabetic
	tokens = [word for word in tokens if word.isalpha()] #solo letras
	# filter out stop words
	stop_words = set(stopwords.words('english'))	
	tokens = [w for w in tokens if not w in stop_words]	
	# filter out short tokens
	tokens = [word for word in tokens if len(word) > 1]	
	l=(' '.join(tokens))	#elimina comilla y coma generada por split() da salida separadas por espacio
	return l

def leer_opinion(path):
	
	dirs = listdir(path)	# Leemos los archivos en el directorio
	opiniones = []	# Definimos una lista que contendra las opiniones
	
	for filename in dirs:	# Iteramos archivo por archivo
		print("Ruta completa", path+filename)
		print("Leido %s \n" % filename)	# Imprimimos
		# Abrimos el archivo en modo lectura
		file = open(path + filename, 'r')
		# Leemos el textop
		text = file.read()
		opiniones.append(text)
		tokens = clean_doc(text)
		f = open(path + filename, 'w') #nuevo directorio
		f.write(str(tokens))
		#print(text)
		# Cerramos el archivo
		file.close()
		f.close();
		print("-------------------\n")

	return opiniones

print("--------OPNINIONES POSITIVAS---------\n")
opiniones_positivas = leer_opinion(path_positivas)

print("--------OPNINIONES NEGATIVAS---------\n")
opiniones_negativas = leer_opinion(path_negativas)

print("--------OPNINIONES POR LISTA---------\n")
print(opiniones_negativas[-1])	# Imprimimos el ultimo elemento
