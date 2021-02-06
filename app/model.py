#./app/model.py

import tensorflow as tf

GEN_PATH=PATH+'models/GAN-generator'

generator = tf.keras.models.load_model(GEN_PATH)

def decode_normalize(img_path):
    img = tf.cast(tf.image.decode_jpeg(tf.io.read_file(img_path)),tf.float32)[...,:3]
    img = img/127.5-1
    return img

def lightUp(img_path):
    dat = tf.data.Dataset.from_tensor_slices([img_path])
    dat = dat.map(decode_normalize)
    dat = dat.batch(1)
    for img in dat:
        HEIGHT = img.shape[1]
        WIDTH = img.shape[2]
        HPAD = (256-HEIGHT%256)%256
        WPAD = (256-WIDTH%256)%256
        # Horizontal bottom border
        row = img[0,-1,...]
        hpad = tf.tile(row[tf.newaxis,...],[HPAD,1,1])[tf.newaxis,...]
        img = tf.keras.layers.Concatenate(axis=1)([img,hpad])
        # Vertical right border
        col = img[0,:,-1,...]
        wpad = tf.tile(col[:,tf.newaxis,...],[1,WPAD,1])[tf.newaxis,...]
        img = tf.keras.layers.Concatenate(axis=2)([img,wpad])
        prediction = generator(img, training=True) # Prediction for input
        
    out = prediction[0]
    out = out[:HEIGHT,:WIDTH]
    return out*0.5+0.5
