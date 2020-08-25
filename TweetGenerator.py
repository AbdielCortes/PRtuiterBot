""" Generates a tweet by picking one string from the pharases array
and inserting it into a string from the sentences array. """

import random

pharases = ["jevos y panas", "la bicha y el caco", "una baby toxica", "un airbnb en el west",
           "esto y un blunt", "dividir los votos", "estadity", "PNPPD", "el bipartidismo",
           "Lugaro vs Dalmau", "la independencia", "Ponce", "empanadilla vs pastelillo", "Bad Bunny",
           "un esquema de piramide", "la colonia", "la estadidad", "Cuba y Venezuela", "el socialismo",
           "el comunismo", "los pelus de la UPR", "la UPR", "Lugaro", "Dalmau", "el PNP"]

sentences = ["Somos %s, pero no estan listos para esa conversacion", "Quisiera que fueramos %s",
             "Gracias a #Forex, logre tener %s", "Odio que en Puerto Rico lo unico que hay es %s",
             "Me cago mil veces en to los pendejos que lo unico que hablan es de %s",
             "Cabron por que no entiendes que es %s, NO es un esquema de piramide",
             "Hablas de %s como si tuiverans un cabron doctorado en eso",
             "El problema de Puerto Rico es %s",
             "Si llego a ver un tweet mas de %s, me voy pal carajo de esta app del pajaro azul"]

def generate_tweet():
    # pick a phrase by generation a random index
    phrase = pharases[random.randint(0, len(pharases)-1)]
    # pick a sentence by generation a random index
    sentence = sentences[random.randint(0, len(sentences)-1)]
    # inserts phrase into sentence
    tweet = sentence % phrase
    return tweet
