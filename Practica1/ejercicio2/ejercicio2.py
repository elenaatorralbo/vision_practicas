import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    exit()

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (width, height))

if not out.isOpened():
    cap.release()
    exit()

print("Grabación iniciada. Presiona 'q' para detener.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv.imshow('Video en tiempo real', frame)

    out.write(frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()

print("Grabación finalizada. El video se guardó como 'output.avi'.")