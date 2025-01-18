import cv2
from src.utils.enums import VideoMode


class VideoHandler():
    def __init__(self,fps = 24,frame_size = (640,480),out_path = 'output/temp/vid.avi'):
        self.out_path = out_path
        self.read_mode = VideoMode.NONE
        self.vid = None
        self.out = None
        # self.__init_camera_read__(frame_size,fps)
    

    def __del__(self):
        self.__release_video__()

    def __init_camera_read__(self,frame_size=(640,480),fps=30):
        print("init camera for reading")
        self.read_mode = VideoMode.CAMERA
        self.vid = cv2.VideoCapture(0)

         # Set the frame width and height
        if frame_size is None:
            frame_size = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print("get frame size: ",frame_size)
        else:    
            self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, frame_size[0])
            self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_size[1])
            print("set frame size: ",frame_size)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        self.out = cv2.VideoWriter(self.out_path, fourcc, fps,frameSize= frame_size) 



    def __release_video__(self):
        if self.out is not None:
            self.out.release()
            self.out = None
            print("Release video recorder")
        if self.vid is not None:
            self.vid.release()
            print("Release video")
        # cv2.destroyAllWindows()

    def set_read_mode(self, mode,vid_path='output/temp/vid.avi'):
        if mode == self.read_mode:
            return
        
        self.__release_video__()
        if VideoMode.VIDEO == mode:
            self.read_mode = VideoMode.VIDEO
            self.vid = cv2.VideoCapture(vid_path)
            self.out = None
        else:
            self.__init_camera_read__()



    def read_frame(self):
        if VideoMode.VIDEO == self.read_mode:
            print("Cannot read frame in video mode. Change video mode to VideoMode.CAMERA")

            return None
        if not self.vid.isOpened():
            print("Failed to open camera.")
            return None
        ret, frame = self.vid.read()
        if not ret:
            print("Failed to read from camera.")
            return None

        # Flip the frame (optional)
        frame = cv2.flip(frame, 1)
        self.out.write(frame)


        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

    def play_video(self):
        if VideoMode.VIDEO == self.read_mode:
            print("Cannot play video in camera mode. Change video mode to VideoMode.VIDEO")
            return
        
        if not self.vid.isOpened():
            print("Failed to open camera.")
            return
        
        _, frame = self.vid.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame   
        

