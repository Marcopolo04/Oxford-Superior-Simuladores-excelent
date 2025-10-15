# Calificador para el examen simulador EXANI-II
# Compara tus respuestas con las correctas y calcula el puntaje

# Lista de respuestas correctas (90 preguntas, en orden: Pensamiento Matemático, Redacción Indirecta, etc.)
respuestas_correctas = [
    'B', 'A', 'B', 'A', 'C', 'A', 'B', 'B', 'B', 'B',  # Pensamiento Matemático (1-10)
    'B', 'B', 'C', 'A', 'B', 'A', 'A', 'B', 'B', 'A',  # Redacción Indirecta (11-20)
    'C', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B',  # Comprensión Lectora (21-30)
    'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B',  # Premedicina (31-40)
    'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A',  # Cálculo Diferencial e Integral (41-50)
    'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A',  # Física (51-60)
    'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',  # Probabilidad (61-70)
    'A', 'B', 'A', 'B', 'A', 'B', 'A', 'C', 'B', 'A',  # Estadística (71-80)
    'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'   # Derecho (81-90)
]

# Instrucciones: Ingresa tus respuestas en esta lista (mismo orden, 90 respuestas en mayúsculas A, B o C)
# Ejemplo: tus_respuestas = ['B', 'A', 'B', ...] (reemplaza con tus respuestas)
tus_respuestas = ['A'] * 90  # Cambia esto por tus respuestas reales

# Verifica que la longitud sea correcta
if len(tus_respuestas) != 90:
    print("Error: Debes ingresar exactamente 90 respuestas.")
else:
    # Calcula aciertos
    aciertos = sum(1 for i in range(90) if tus_respuestas[i].upper() == respuestas_correctas[i])
    porcentaje = (aciertos / 90) * 100
    
    # Muestra resultados
    print(f"Resultados del examen EXANI-II:")
    print(f"Aciertos: {aciertos}/90")
    print(f"Porcentaje: {porcentaje:.1f}%")
    
    # Retroalimentación básica
    if porcentaje >= 80:
        print("¡Excelente! Estás bien preparado.")
    elif porcentaje >= 60:
        print("Buen trabajo, pero repasa las áreas débiles.")
    else:
        print("Necesitas practicar más. ¡Ánimo!")

# Opcional: Imprime errores por pregunta
# for i in range(90):
#     if tus_respuestas[i].upper() != respuestas_correctas[i]:
#         print(f"Pregunta {i+1}: Tu respuesta: {tus_respuestas[i]}, Correcta: {respuestas_correctas[i]}")
