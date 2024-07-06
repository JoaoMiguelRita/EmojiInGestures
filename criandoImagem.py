from PIL import Image, ImageDraw

# Criar uma nova imagem RGB (vermelho, verde, azul)
width, height = 200, 200
image = Image.new('RGB', (width, height), color = (255, 255, 255))

# Desenhar um círculo vermelho no centro
draw = ImageDraw.Draw(image)
draw.ellipse((50, 50, 150, 150), fill=(255, 0, 0))

# Salvar a imagem
image.save('image.jpg')
print("Imagem 'image.jpg' criada com sucesso.")
