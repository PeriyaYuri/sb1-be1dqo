import cv2
import time
from video_stream import VideoStream
from human_detector import HumanDetector
from display import Display
from watchdog import StreamWatchdog

def main():
    # Конфигурация камер
    camera_configs = [
        {"url": "rtsp://camera1_ip:554/stream1", "id": 1},
        {"url": "rtsp://camera2_ip:554/stream2", "id": 2}
    ]
    
    # Инициализация компонентов
    streams = [VideoStream(cfg["url"], cfg["id"]) for cfg in camera_configs]
    detector = HumanDetector()
    display = Display([f"Camera {stream.camera_id}" for stream in streams])
    watchdog = StreamWatchdog(streams)
    
    try:
        while True:
            # Проверка состояния потоков
            watchdog.check_streams()
            
            # Обработка каждого потока
            for i, stream in enumerate(streams):
                success, frame = stream.read_frame()
                
                if success and frame is not None:
                    # Детекция людей
                    boxes = detector.detect(frame)
                    
                    # Отрисовка результатов
                    frame = detector.draw_detections(frame, boxes)
                    
                    # Отображение кадра
                    display.show_frame(f"Camera {stream.camera_id}", frame)
            
            # Проверка нажатия клавиши выхода
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
            # Небольшая задержка для снижения нагрузки на процессор
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("\nЗавершение работы...")
    finally:
        # Освобождение ресурсов
        for stream in streams:
            stream.release()
        display.destroy_windows()

if __name__ == "__main__":
    main()