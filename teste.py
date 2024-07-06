import cv2

# Carregar a imagem
img = cv2.imread("image.jpg")

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
else:
    # Exibir a imagem
    cv2.imshow("Imagem", img)
    cv2.waitKey(0)  # Espera uma tecla ser pressionada
    cv2.destroyAllWindows()  # Fecha a janela
