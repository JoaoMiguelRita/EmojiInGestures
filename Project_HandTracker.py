import os
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import numpy as np
import warnings
import logging

# Suprimir avisos do TensorFlow Lite
logging.getLogger('tensorflow').setLevel(logging.ERROR)

# Suprimir avisos do protobuf
warnings.filterwarnings('ignore', category=UserWarning, module='google.protobuf.symbol_database')

# Função para desenhar os marcos na imagem
def draw_landmarks_on_image(image, detection_result):
    for hand_landmarks in detection_result.hand_landmarks:
        for landmark in hand_landmarks:
            cv2.circle(image, (int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])), 5, (0, 255, 0), -1)
    return image

# Caminho para o modelo
model_path = 'C:\\Users\\USER\\Desktop\\Hand_Tracker\\hand_landmarker.task'

# Verifique se o arquivo de modelo existe
if not os.path.exists(model_path):
    print(f"Erro: o arquivo de modelo '{model_path}' não foi encontrado.")
else:
    # STEP 1: Crie o objeto HandLandmarker
    base_options = python.BaseOptions(model_asset_path=model_path)
    options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
    detector = vision.HandLandmarker.create_from_options(options)

    # Inicializar a captura de vídeo da câmera
    cap = cv2.VideoCapture(0)

    # Verifique se a câmera foi aberta com sucesso
    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
    else:
        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    print("Erro ao capturar a imagem da câmera.")
                    break

                # Converter o frame do OpenCV (BGR) para RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Criar uma imagem mediapipe a partir do frame RGB
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(frame_rgb))

                # Detectar marcos da mão no frame
                detection_result = detector.detect(mp_image)

                # Desenhar os marcos na imagem
                annotated_image = draw_landmarks_on_image(frame, detection_result)

                # Mostrar a imagem anotada
                cv2.imshow("Hand Landmarks", annotated_image)

                # Sair do loop se a tecla 'q' for pressionada
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            # Liberar a captura e destruir todas as janelas
            cap.release()
            cv2.destroyAllWindows()
