import cv2  # OpenCV principal

def createROI(imagen, x, y, ancho, alto):

    if x < 0 or y < 0 or x + ancho > imagen.shape[1] or y + alto > imagen.shape[0]:
        print(
            f"Error: ROI excede límites. Imagen shape: {imagen.shape}. Ajusta x={x}, y={y}, ancho={ancho}, alto={alto}.")
        return None
    return imagen[y:y + alto, x:x + ancho]  # Slicing: filas (y) y columnas (x)



nombre_imagen = '/home/elenaa/vision_practicas/DIP4E Book Images Global Edition/lena.tif'  # O 'lena.png' si así lo descargaste
imagen_original = cv2.imread(nombre_imagen)

if imagen_original is None:
    print(f"Error: No se pudo cargar '{nombre_imagen}'.")
else:
    print(f"Imagen cargada exitosamente. Dimensiones: {imagen_original.shape} ")

    cv2.imshow('Imagen Original', imagen_original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  # Cierra ventanas

    # Paso 3: Extraer y guardar ROIs diferentes (experimentos como pide el ejercicio)
    # ROI 1: Esquina superior izquierda (x=0, y=0) - Enfocado en sombrero y parte del rostro
    roi1 = createROI(imagen_original, x=0, y=0, ancho=400, alto=400)
    if roi1 is not None:
        cv2.imshow('ROI 1: Superior Izquierda', roi1)
        cv2.imwrite('roi1_superior_izquierda.png', roi1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("ROI 1 guardado")

    # ROI 2: Centro aproximado (para Lenna 512x512, centro en ~56,56)
    x_centro = (imagen_original.shape[1] - 400) // 2  # ~56
    y_centro = (imagen_original.shape[0] - 400) // 2  # ~56
    roi2 = createROI(imagen_original, x=x_centro, y=y_centro, ancho=400, alto=400)
    if roi2 is not None:
        cv2.imshow('ROI 2: Centro', roi2)
        cv2.imwrite('roi2_centro.png', roi2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("ROI 2 guardado ")

    # ROI 3: Parte inferior derecha (ej: x=112, y=112) - Enfocado en hombro y fondo
    # Modifícalo aquí para experimentar: cambia x, y, ancho/alto
    roi3 = createROI(imagen_original, x=112, y=112, ancho=400, alto=400)
    if roi3 is not None:
        cv2.imshow('ROI 3: Inferior Derecha (modificable)', roi3)
        cv2.imwrite('roi3_inferior_derecha.png', roi3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("ROI 3 guardado")


