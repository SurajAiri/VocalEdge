from enum import Enum


class AppScreen(Enum):
    HOME = 0
    PARTICIPATE = 1
    RESULT = 2
    ABOUT = 3

class AudioMode(Enum):
    NOT_RECORDING = 0
    RECORDING = 1

class VideoMode(Enum):
    NONE = 0
    VIDEO = 1
    CAMERA = 2

