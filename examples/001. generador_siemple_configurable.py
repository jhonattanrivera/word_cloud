#!/usr/bin/env python
from os import path
import os
import nltk

import matplotlib.pyplot as plt
from wordcloud import WordCloud #, STOPWORDS

# Descarga un listado de stopwords en distintos idiomas
# en este caso, español; se pueden usar varios diccionarios
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = set(stopwords.words('spanish'))
stopwords.update(["Media","omitted","1","2","3","4","5","6","7","8","9","0","/","AM","PM","-"])
#stopwords.discard("qué") # Eilimina una palabra de las stopwords para que sea tenida en cuanta

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'compilado.txt'),encoding="utf-8").read()

# Genera el wordcloud con parámetros adicionales disponibles en la documentación
wc = WordCloud(background_color="white",max_words=500,width=4000,height=2000,repeat=False,
               stopwords=stopwords,contour_width=3,contour_color='steelblue')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "output.png"))

# show
plt.figure()
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()