import pbkdf2, base64, os, sys

def generate_hash(password):
	#Descomentar estas dos líneas y copiar la linea b'xxxxxxxxxxxxxxxxxxxxxxx' en passwordSalt para usar una sal diferente
	#passwordSalt = os.urandom(16)
	#print(passwordSalt)
	passwordSalt = b'{\x16j\xa3\xee\xf4;\xe3\xa3\xaa\xe1m\xa4H\x9f\xf7'
	key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
	# se puede modificar por b64encode para menos simbolos y por b16encode para solo numeros y mayusculas
	new_psw = base64.b16encode(key)
	new_psw = new_psw.decode()[:28]
	separator = "-"
	res = "" 
	count = 0
	for i in range(0, len(new_psw), 4): 
    		count += 1
    		if count % 2 == 0:
        		res += new_psw[i:i + 4] + separator 
    		else: 
        		res += new_psw[i:i + 4].lower() + separator
	# Remove the trailing separator 
	res = res[:-1] 
	# printing result    
	return res

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
