import cv2
import numpy as np
from typing import List, Tuple

class HumanDetector:
    def __init__(self):
        # Инициализация HOG-детектора людей
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self, frame: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """Обнаружение людей на кадре"""
        # Уменьшаем размер кадра для ускорения обработки
        frame = cv2.resize(frame, (640, 480))
        
        # Обнаружение людей
        boxes, weights = self.hog.detectMultiScale(
            frame, 
            winStride=(8, 8),
            padding=(4, 4),
            scale=1.05
        )
        
        return boxes.tolist()

    def draw_detections(self, frame: np.ndarray, boxes: List[Tuple[int, int, int, int]]) -> np.ndarray:
        """Отрисовка обнаруженных людей на кадре"""
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame