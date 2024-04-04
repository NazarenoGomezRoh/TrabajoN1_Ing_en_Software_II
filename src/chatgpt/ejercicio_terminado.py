"""
Este es un programa que utiliza la API de OpenAI para interactuar con el modelo ChatGPT.
"""

import sys  # Importar la biblioteca sys para acceder a los argumentos de línea de comandos
import openai
import pyreadline

# Configurar la clave API de OpenAI
openai.api_key = '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'  # Recuerda reemplazar con tu clave API

# Variable para almacenar la última consulta
last_query = ""

def chat_gpt_response(context, user_task, user_query):
    """
    Obtiene la respuesta del modelo ChatGPT para una consulta dada.

    Args:
        context (str): Contexto previo.
        user_task (str): Tarea del usuario.
        user_query (str): Consulta del usuario.

    Returns:
        str: Respuesta generada por el modelo ChatGPT.
    """
    try:
        # Llamar a la API de ChatGPT con la estructura proporcionada
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",  # Modelo de ChatGPT a utilizar
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_task},
                {"role": "user", "content": user_query}
            ],
            temperature=1,
            max_tokens=4096,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        print("Se produjo un error al invocar la API de ChatGPT:", e)
        return None


def main():
    """
    Función principal del programa.
    """
    # Verificar si se ha proporcionado el argumento "--convers"
    if "--convers" in sys.argv:
        convers_mode = True
        buffer = []  # Inicializar un buffer para almacenar las consultas y respuestas
    else:
        convers_mode = False

    last_query = ""  # Variable para almacenar la última consulta

    while True:
        try:
            # Aceptación de la consulta del usuario
            user_query = input("Ingrese su consulta: ")

            # Verificar si la consulta tiene texto
            if user_query.strip():
                # Imprimir la consulta con etiqueta "You:"
                print("You:", user_query)

                # Tratamiento de la consulta
                context = " ".join(buffer) if convers_mode else "contexto previo"
                user_task = "tarea del usuario"

                # Actualizar la última consulta
                last_query = user_query

                # Invocación de la API de ChatGPT
                response = chat_gpt_response(context, user_task, last_query)

                # Imprimir la respuesta con etiqueta "chatGPT:"
                if response:
                    print("chatGPT:", response)
                    if convers_mode:
                        buffer.append(last_query)
                        buffer.append(response)
                else:
                    print("No se pudo obtener una respuesta.")
            else:
                print("Por favor, ingrese una consulta válida.")

        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            break
        except openai.OpenAIError as e:
            print("Se produjo un error:", e)


if __name__ == "__main__":
    main()
