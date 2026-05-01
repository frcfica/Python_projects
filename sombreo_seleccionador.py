def sombrero_seleccionador():
    puntajes = {
        "Gryffindor": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0,
        "Slytherin": 0
    }
print("==|Bienvenido al sombrero seleccionador|==")
print("Responde las siguientes preguntas para descubrir a qué casa de Hogwarts perteneces.")
preguntas = [
    {   # Pregunta 1
        "pregunta": "Como te definiirias mejor?",
        "opciones": [
            ("Valiente","Gryffindor"),
            ("Leal","Hufflepuff"),
            ("Sabio", "Ravenclaw"),
            ("Ambicioso", "Slytherin")
        ]
    },
    {   # Pregunta 2
        "pregunta": "Que animal te gusta mas?",
        "opciones": [
            ("Leon", "Gryffindor"),
            ("Tejon", "Hufflepuff"),
            ("Aguila", "Ravenclaw"),
            ("Serpiente", "Slytherin")
        ]
    },
    {   # Pregunta 3
        "pregunta": "En un duelo de magos, tu...",
        "opciones": [
            ("Atacas de frente con coraje", "Gryffindor"),
            ("Proteges a tus amigos", "Hufflepuff"),
            ("Usas un hechizo ingeniso y complejo", "Ravenclaw"),
            ("Haces lo que sea necesario para ganar", "Slytherin")
        ]
    },
    {   # Pregunta 4
        "pregunta": "Que tipo de magia te atrae mas estudiar?",
        "opciones": [
            ("Defensa contra las artes oscuras", "Gryffindor"),
            ("Herbologia o cuidado de criaturas magicas", "Hufflepuff"),
            ("Astronomia o runas antiguas", "Ravenclaw"),
            ("Pociones o artes oscuras", "Slytherin")
        ]
    }
]
for p in preguntas: # Ciclo para recorrer las preguntas 
    print (p["pregunta"])
    for i, (texto, casa) in enumerate(p["opciones"], 1):
        print(f"{i}. {texto}")
        