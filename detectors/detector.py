'''
Detectors entry point.
'''

# pylint: disable=import-outside-toplevel


def get_bounding_boxes(frame, model):
    '''
    Run object detection algorithm and return a list of bounding boxes and other metadata.
    '''
    if model == 'yolo':
        from detectors.yolo import get_bounding_boxes as gbb
    elif model == 'haarcascade':
        from detectors.haarcascade import get_bounding_boxes as gbb
    elif model == 'tfoda':
        from detectors.tfoda import get_bounding_boxes as gbb
    elif model == 'detectron2':
        from detectors.detectron2 import get_bounding_boxes as gbb
    else:
        raise Exception('Invalid detector model, algorithm or API specified (options: yolo, tfoda, detectron2, haarcascade)')

    return gbb(frame)
