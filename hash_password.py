# Importa el módulo sys para manejar argumentos de línea de comandos y salida del programa
import sys

# Importa la biblioteca bcrypt para realizar hashing seguro de contraseñas
import bcrypt

# Función para generar un hash seguro de una contraseña proporcionada
def generate_hash(password):
    # Genera una "sal" aleatoria para mejorar la seguridad del hash
    salt = bcrypt.gensalt()
    # Cifra la contraseña combinándola con la sal generada, codificando la contraseña a bytes
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Devuelve el hash generado como una cadena de texto (decode para convertir bytes a str)
    return hashed_password.decode('utf-8')

# Bloque principal: solo se ejecuta si el script es ejecutado directamente
if __name__ == "__main__":
    # Verifica si se ha proporcionado al menos un argumento (la contraseña)
    if len(sys.argv) < 2:
        # Muestra un mensaje de error si no se proporciona la contraseña
        print("Error: Se requiere una contraseña como argumento")
        # Termina la ejecución del programa con un código de error 1
        sys.exit(1)

    # Obtiene la contraseña proporcionada como argumento desde la línea de comandos
    password = sys.argv[1]
    # Genera el hash seguro de la contraseña proporcionada
    hashed_password = generate_hash(password)
    # Imprime el hash generado en la consola
    print(hashed_password)
