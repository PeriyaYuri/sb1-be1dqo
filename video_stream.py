import cv2
import time
from typing import Optional, Tuple

class VideoStream:
    def __init__(self, camera_url: str, camera_id: int):
        self.camera_url = camera_url
        self.camera_id = camera_id
        self.stream = None
        self.connect()
    
    def connect(self) -> None:
        """Подключение к IP камере"""
        try:
            self.stream = cv2.VideoCapture(self.camera_url)
            if not self.stream.isOpened():
                raise Exception(f"Не удалось подключиться к камере {self.camera_id}")
        except Exception as e:
            print(f"Ошибка подключения к камере {self.camera_id}: {str(e)}")
            self.stream = None

    def read_frame(self) -> Tuple[bool, Optional[np.ndarray]]:
        """Чтение кадра с камеры"""
        if self.stream is None:
            return False, None
        
        ret, frame = self.stream.read()
        if not ret:
            self.reconnect()
            return False, None
        return True, frame

    def reconnect(self) -> None:
        """Переподключение к камере при потере связи"""
        print(f"Переподключение к камере {self.camera_id}...")
        self.release()
        time.sleep(2)
        self.connect()

    def release(self) -> None:
        """Освобождение ресурсов камеры"""
        if self.stream is not None:
            self.stream.release()
            self.stream = None