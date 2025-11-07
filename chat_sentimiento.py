import random
from deep_translator import GoogleTranslator
from textblob import TextBlob

#lista de saludos y respuestas
saludos=["hola","que tal","buenos dias","buenas tardes","buenas noches"]
respuestas=["hola, como estas?",
            "como puedo ayudarte",
            "hola como te va",
            "que hay?"]
#mensaje de bienvenida del chatbot
print("Hola soy Chato, tu chabot de confianza, si deseas"
      "terminar escribe salir")

entimiento=["me siento enojado","me siento feliz","me siento triste",]
respuesta_feliz=["que bien me alegro"]
respuesta_triste=["que mal","espero te mejore pronto"]
salir=["adios"]




while True:
    usuario=input("Tu:").lower().strip()
    trad=GoogleTranslator(source="auto",target="en").translate(usuario)
    analizar=TextBlob(trad)
    print("polaridad",analizar.polarity)
    if analizar.polarity>0:
        respuesta_feliz.append(trad)
        print("chatbot:",random.choice(respuesta_feliz))
    elif analizar.polarity<0:
        respuesta_triste.append(trad)
        print("chatbot:",random.choice(respuesta_triste))
    elif usuario in salir:
        break
