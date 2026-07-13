from ultralytics import YOLO
import cv2
def new_win():
    model = YOLO("yolov8n.pt")


    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cv2.namedWindow("Hoshang Vision 👁️", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("no frame")
            break

            frame_small = cv2.resize(frame, (640, 640))
            results = model(frame_small, conf=0.5, verbose=False)
            frame_plot = results[0].plot()
            frame_plot = cv2.resize(frame_plot, (frame.shape[1], frame.shape[0]))  #  # برگرداندن به سایز اصلی


        cv2.imshow("Hoshang Vision 👁️", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
