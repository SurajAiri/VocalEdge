import cv2

vid = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output_vid.avi', fourcc, 20.0, (frame_width, frame_height))

while vid.isOpened():
    ret, frame = vid.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv2.flip(frame, 1)
    cv2.imshow('frame', frame)
    # print(frame.shape)
    # write the flipped frame
    out.write(frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
out.release()
vid.release()
cv2.destroyAllWindows()