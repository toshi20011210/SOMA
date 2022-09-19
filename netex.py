from keras import backend as K
from keras.datasets import mnist
import matplotlib.pyplot as plt
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("画像データの要素数", train_images.shape)
print("ラベルデータの要素数", train_labels.shape)
for i in range(0,10):
 print("ラベル", train_labels[i])
 plt.imshow(train_images[i].reshape(28, 28), cmap='Greys')
 plt.show()