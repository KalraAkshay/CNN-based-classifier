import numpy as np
from keras.preprocessing import image
from keras.models import load_model

test_image = image.load_img(r'parent\cat\cat.6.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
model = load_model('dog_cat_model.h5')
result = model.predict(test_image)
print(training_set.class_indices)
if result[0][0] == 1:
    prediction = 'dog'
    print(prediction)
else:
    prediction = 'cat'
    print(prediction)
