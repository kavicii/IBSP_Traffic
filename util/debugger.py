'''
Utilities for configuring and debugging the vehicle count process.
'''

import cv2

from .logger import get_logger
import settings

logger = get_logger()

class CoordinateStore:
    
    def __init__(self):
        self.points = []
    
    def mouse_callback(self, event, x, y, flags, param):
        '''
        Handler for mouse events in the debug window.
        '''
        if event == cv2.EVENT_LBUTTONDOWN:
            self.capture_pixel_position(x, y, param['frame_width'], param['frame_height'])

    def capture_pixel_position(self, window_x, window_y, frame_w, frame_h):
            '''
            Capture the position of a pixel in a video frame.
            '''
            debug_window_size = settings.DEBUG_WINDOW_SIZE
            x = round((frame_w / debug_window_size[0]) * window_x)
            y = round((frame_h / debug_window_size[1]) * window_y)
            logger.info('Pixel position captured.', extra={'meta': {'label': 'PIXEL_POSITION', 'position': (x, y)}})
            self.points.append((x,y))
            