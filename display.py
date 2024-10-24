import cv2
import numpy as np
from typing import List

class Display:
    def __init__(self, window_names: List[str]):
        self.window_names = window_names
        self.setup_windows()
    
    def setup_windows(self) -> None:
        """Создание окон для отображения"""
        for name in self.window_names:
            cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    
    def show_frame(self, window_name: str, frame: np.ndarray) -> None:
        """Отображение кадра в указанном окне"""
        if frame is not None:
            cv2.imshow(window_name, frame)
    
    def destroy_windows(self) -> None:
        """Закрытие всех окон"""
        cv2.destroyAllWindows()