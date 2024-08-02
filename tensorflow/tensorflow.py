import numpy as np
import matplotlib.pyplot as plt
import keras
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Conv2D, BatchNormalization, LeakyReLU, Reshape, Conv2DTranspose, Input

# Função para gerar dados de exemplo (foto antiga em tons de cinza)
def generate_gray_images(batch_size=10, shape=(64, 64, 1)):
    return np.random.rand(batch_size, *shape)

# GAN para restauração e colorização
def build_restoration_gan():
    model = Sequential()

    # Encoder
    model.add(Conv2D(64, kernel_size=3, strides=2, input_shape=(64, 64, 1), padding='same'))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha=0.2))

    # Decoder
    model.add(Conv2DTranspose(64, kernel_size=3, strides=2, padding='same'))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2D(1, kernel_size=3, activation='sigmoid', padding='same'))

    return model

# Exemplo de uso
batch_size = 1

# Geração de dados de entrada (tons de cinza)
gray_images = generate_gray_images(batch_size)

# Construção e compilação do modelo GAN de restauração
restoration_gan = build_restoration_gan()
restoration_gan.compile(loss='mse', optimizer='adam')

# Treinamento (neste exemplo, usamos os mesmos dados como entrada e saída, pois é um exemplo simples)
restoration_gan.fit(gray_images, gray_images, epochs=50, batch_size=batch_size)

# Geração de imagens restauradas
restored_images = restoration_gan.predict(gray_images)

# Visualização das imagens
plt.figure(figsize=(10, 5))

# Imagem original em tons de cinza
plt.subplot(1, 3, 1)
plt.imshow(gray_images[0, :, :, 0], cmap='gray')
plt.title('Imagem Original (Tons de Cinza)')

# Imagem restaurada pela GAN
plt.subplot(1, 3, 2)
plt.imshow(restored_images[0, :, :, 0], cmap='gray')
plt.title('Imagem Restaurada')

# Imagem colorida (exemplo simples)
colored_image = np.zeros((64, 64, 3))
colored_image[:, :, 0] = gray_images[0, :, :, 0]  # Canal R
colored_image[:, :, 1] = restored_images[0, :, :, 0]  # Canal G
colored_image[:, :, 2] = gray_images[0, :, :, 0]  # Canal B

plt.subplot(1, 3, 3)
plt.imshow(colored_image)
plt.title('Imagem Colorida (Exemplo Simples)')

plt.show()
