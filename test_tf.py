import tensorflow as tf

# Create a simple tensor
tensor = tf.constant([[1, 2], [3, 4]])

print("Tensor:")
print(tensor)

print("\nTensor shape:")
print(tensor.shape)

print("\nTensor datatype:")
print(tensor.dtype)

# Simulating an image tensor (height=224, width=224, channels=3)
image_tensor = tf.random.uniform((224, 224, 3))

print("\nImage Tensor Shape:")
print(image_tensor.shape)