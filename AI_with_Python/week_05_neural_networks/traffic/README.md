# ABOUT THIS PROJECT - Tuning parameters

This document contains a brief explanation on how I ended up in the final model.


**NOTE:** Upon writing this document, I am a beginner in neural networks / TensorFlow. So my conclusions might not be accurate. I will keep learning, and maybe this file can be updated at some point 😉

**Demonstration of the model** available on [Youtube](https://youtu.be/sR7f6TlZK5Q)

## The steps

**1. I started by running the model with the following settings:**

    > - one convolutional layer, with 32 filters, 3x3 kernel
    > - one Max-pooling layer, using 2x2 pool size
    > - one dense hidden layer with 128 nodes, activation=relu, with 0.5 dropout

 
However this model only gave me an accuracy of about 5%. Therefore I move to tune the paremeters and experiment a bit.

  
**2. The next thing I tried was to increase the number of layers to the same number of categories.**

This increased the efficiency of the model from (0.0536 to 0.1664). It was a big improvement, but still not quite good enough. So I decided to double the initial number of layers, using 64. However, this model performed poorly compared to model #2. Therefore, I decide to stick to 43 layers, and move to further experiements.

**3. Tweeking the kernel and pooling layer**

As I have very small images (30x30 pixels), I wanted to run the model with a smaller kernel (2x2). I didn’t get any satisfactory results, so I applied a smaller pool size as well (1x1). Of course, in this case the pooling doesn't make any sense, but why not try - I am a beginner, don't judge me! 🙈 Likewise the previous situation, the performance was poor and the time to run increased considerably. Because of that, I returned to values 43 layers, kernel 3x4, pooling 2x2.

**4. Experimenting with dropout values**

Next, I decided to remove the number of dropouts. With a relatively small dataset, I cannot have the luxury of dropping too many values!

I reduced the dropout to 0.25. Still, the model performed poorly.

**5. Hidden layers, here I come!**

Therefore I moved to increase the number of hidden layers, which ultimaly led me to a model with over 90% accuracy.

I experimented with different number of hidden layers (varying from 1 to 6), different values of layers, and I also tweeked the values on steps 2 - 4 again.Increasing the number of layers increased the accuracy of my model, however increasing the number of nodes within a layer played a role as well.

I also tested a different activation for the sub-sequential layers (softmax), but the model performed poorly with those tweeks. Below the results of a few of these experimentations:

  

> **2 hidden layers, one dropout 0.5**
> 333/333 - 2s - loss: 0.3593 - accuracy: 0.9431 - 2s/epoch - 5ms/step
> model_43L_3x3_pool_2x2_2dense256_dropout_dot5.h5
> 
> 
> **4 hidden layers, one dropout 0.5**
> 333/333 - 2s - loss: 0.3790 - accuracy: 0.9318 - 2s/epoch - 6ms/step
> model_43L_3x3_pool_2x2_4dense256_dropout_dot5.h5
> 
> 
> **4 hidden, one dropout 0.5**
> 333/333 - 2s - loss: 0.3835 - accuracy: 0.9115 - 2s/epoch - 7ms/step
> model_43L_3x3_pool_2x2_4dense128_dropout_dot5.h5


**6. The final model**

In the end, the final model was set with:

    - one convolutional layer, with 43 filters, 3x3 kernel (number of filters = number of image categories)
    - one Max-pooling layer, using 2x2 pool size
    - one dense hidden layer with 256 nodes, activation=relu
    - second dense hidden layer with 256 nodes, activation=relu, with 0.5 dropout



The results of the training are summarised below:


    Epoch 1/10
    500/500 [==============================] - 13s 25ms/step - loss: 6.5720 - accuracy: 0.1540
    
    Epoch 2/10
    500/500 [==============================] - 13s 26ms/step - loss: 1.9825 - accuracy: 0.4103
    
    Epoch 3/10
    500/500 [==============================] - 13s 26ms/step - loss: 1.3249 - accuracy: 0.6019
    
    Epoch 4/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.9059 - accuracy: 0.7419
    
    Epoch 5/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.6121 - accuracy: 0.8255
    
    Epoch 6/10
    
    500/500 [==============================] - 13s 25ms/step - loss: 0.5290 - accuracy: 0.8534
    
    Epoch 7/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.4184 - accuracy: 0.8888
    
    Epoch 8/10
    500/500 [==============================] - 14s 27ms/step - loss: 0.4049 - accuracy: 0.8973
    
    Epoch 9/10
    500/500 [==============================] - 14s 27ms/step - loss: 0.3243 - accuracy: 0.9150
    
    Epoch 10/10
    500/500 [==============================] - 14s 27ms/step - loss: 0.2875 - accuracy: 0.9259
    
    333/333 - 2s - loss: 0.4076 - accuracy: 0.9141 - 2s/epoch - 6ms/step



**7. Accounting for overfitting**

As the assigment goes, I am not allowed to modify the main function. However I still wanted to take some steps to tackle the issue of overfitting.

After reading several tutorials online, I decided to use matplotlib to plot two graphs just to make sure my model was not overfitting.

The final plots can be seen in the image below. I still need to learn more about this step though!

<img  scr="static/figure_1.png"  width="80%">

## The takeways

 - The simpler the model the better
 - A kernel size of 3x3 is probably small enough
 - Reducing the dropout can increase performance, but watch out for overfitting
 - Keep learning, it was fun! 👩‍💻 🤓