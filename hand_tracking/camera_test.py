import cv2

for i in range(3):  # Try camera indexes 0, 1, 2
    print(f"Trying camera index {i}...")
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera index {i} is available.")
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame!")
                break
            cv2.imshow(f"Camera {i} (press q to quit)", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        break
    else:
        print(f"Camera index {i} is not available.")
        cap.release()
