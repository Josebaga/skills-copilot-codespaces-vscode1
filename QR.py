import cv2
from pyzbar.pyzbar import decode

def qr_to_text(image_path):
    # Cargar la imagen
    image = cv2.imread(image_path)
    
    # Decodificar el QR
    decoded_objects = decode(image)
    
    # Extraer y devolver el texto
    for obj in decoded_objects:
        return obj.data.decode('utf-8')
    
    return "No se encontró un código QR en la imagen."

# Ejemplo de uso
if __name__ == "__main__":
    image_path = "qr_code.png"  # Reemplaza con la ruta de tu imagen
    text = qr_to_text(image_path)
    print("Texto extraído del QR:", text)