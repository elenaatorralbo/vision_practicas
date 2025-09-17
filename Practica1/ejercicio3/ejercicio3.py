import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def calculateBrightnessContrast(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    contrast = np.std(gray)
    return brightness, contrast

def calculateBrightnessContrastManual(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    height, width = gray.shape
    total_pixels = height * width
    brightness = np.sum(gray) / total_pixels
    mean_diff = np.abs(gray - brightness)
    contrast = np.mean(mean_diff)
    return brightness, contrast

cap = cv.VideoCapture(0)
if not cap.isOpened():
    exit()

hist_b_list = []
hist_g_list = []
hist_r_list = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    bright_auto, contrast_auto = calculateBrightnessContrast(frame)
    bright_manual, contrast_manual = calculateBrightnessContrastManual(frame)
    print(f"Brillo (auto): {bright_auto:.2f}, Contraste (auto): {contrast_auto:.2f}")
    print(f"Brillo (manual): {bright_manual:.2f}, Contraste (manual): {contrast_manual:.2f}")

    b, g, r = cv.split(frame)

    hist_b = cv.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv.calcHist([r], [0], None, [256], [0, 256])
    hist_b_list.append(hist_b)
    hist_g_list.append(hist_g)
    hist_r_list.append(hist_r)

    cv.imshow('Video en tiempo real', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

if hist_b_list:
    avg_hist_b = np.mean(hist_b_list, axis=0)
    avg_hist_g = np.mean(hist_g_list, axis=0)
    avg_hist_r = np.mean(hist_r_list, axis=0)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'histogramas_promedio_{timestamp}.png'

    plt.figure(figsize=(8, 5))
    plt.title('Histogramas Promedio de Intensidad (B, G, R)')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia Promedio')
    plt.xlim(0, 255)
    plt.ylim(0, max(max(avg_hist_b.max(), avg_hist_g.max(), avg_hist_r.max()) * 1.1, 1000))  # Ajuste dinámico
    plt.plot(range(256), avg_hist_b, color='blue', label='Canal B')
    plt.plot(range(256), avg_hist_g, color='green', label='Canal G')
    plt.plot(range(256), avg_hist_r, color='red', label='Canal R')
    plt.legend()

    plt.savefig(filename, dpi=300, bbox_inches='tight')

    plt.show(block=True)

    print(f"Gráfico generado y guardado como '{filename}'. Cierra la ventana del gráfico para finalizar.")
else:
    print("No se capturaron fotogramas para generar el gráfico.")

print("Programa finalizado.")