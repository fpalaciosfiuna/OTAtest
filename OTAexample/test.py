import cv2

# Inicializa la captura de video desde la webcam
cap = cv2.VideoCapture(0)

# Verifica si la cámara se ha abierto correctamente
if not cap.isOpened():
    print("Error: No se puede acceder a la cámara.")
    exit()

# Bucle para capturar y mostrar las imágenes
while True:
    # Captura un frame de la cámara
    ret, frame = cap.read()

    # Si se ha capturado correctamente
    if not ret:
        print("Error: No se pudo leer el frame.")
        break

    # Redimensiona el frame a un tamaño más pequeño (por ejemplo, 640x480)
    frame_resized = cv2.resize(frame, (640, 480))

    # Muestra el frame redimensionado en una ventana
    cv2.imshow('Ventana de la Webcam', frame_resized)

    # Espera a que presiones la tecla 'q' para cerrar la ventana
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra todas las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()


