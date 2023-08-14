import cv2
import numpy as np
import os
import sys
import tensorflow as tf
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )


    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """

    # start a list of images and labels
    images = list()
    labels = list()

    for category in range(NUM_CATEGORIES):

        # NOTE: use os.path.join and os.sep so that code if platform-independent

        #print(category)

        full_path_category = os.path.join(data_dir, str(category)) #creates the full path of the category

        for file in os.listdir(full_path_category): # for each file in the folder
            image_path = os.path.join(full_path_category, file) # full path for the file

            image = cv2.imread(image_path) # reads the image
            #print(image_path)
            image_resized = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT)) # resizes the image

            images.append(image_resized) # adds resized imaged to the list of images
            labels.append(category) # adds category to the list of categories

    #print(len(images))
    #print(len(labels))

    # convert lists to numpy arrays for easier processing
    # note: this is done in main, but good practice to do it here in case was not done in main
    np_image = np.array(images)
    np_labels = np.array(labels)

    return (np_image, np_labels)   #return tupple  (images, labels)



def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """

    # code from lecture: create a convolutional neural network

    # A sequential model is a linear stack of layers,
    # where each layer has exactly one input tensor and one output tensor.
    # so in this case, input = output = NUM_CATEGORIES
    model = tf.keras.models.Sequential([

    # Convolutional layer. Learn X filters using a i x j kernel
    tf.keras.layers.Conv2D(
        NUM_CATEGORIES, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        #EXPLANATION
        # activation relu: return 0 if value <0 or value, if value >= 0
        # input shape: width, height, and 3 color channels (RGB).
    ),

    # Max-pooling layer, using 2x2 pool size
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Flatten units
    tf.keras.layers.Flatten(),

    # Add a hidden layer
    tf.keras.layers.Dense(256, activation="relu"),

    # Add a second hidden layer with dropout
    tf.keras.layers.Dense(256, activation="relu"),
    tf.keras.layers.Dropout(0.25),

    # Add an output layer with output units for all categories
    tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    # Train neural network
    model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
    )

    return model #return model trained

def plot_history(history):
    plt.figure(figsize=(12, 4))

    # Plot training & validation loss
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Train')
    plt.plot(history.history['val_loss'], label='Validation')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    # Plot training & validation accuracy
    plt.subplot(1, 2, 2)
    plt.plot(history.history['accuracy'], label='Train')
    plt.plot(history.history['val_accuracy'], label='Validation')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.show()

def model_no_overfitting():
    # Split data into train, validation, and test sets
    train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)
    train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.2, random_state=42)

    # Get a compiled neural network
    model = get_model()

    # adds a stop, that helps to prevent overfitting
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

    # fits the model on training data
    history = model.fit(x_train, y_train, epochs=EPOCHS, batch_size=32, validation_data=(val_images, val_labels), callbacks=[early_stopping])

    # plots graph with losses and accuracy
    plot_history(history)

if __name__ == "__main__":
    main()
