# Testing and Training Data

At this course we use generated data to create 3 random spiral classes data. The expectation to predict classes of additional generated data.

The complexity of neural networks is their biggest issue and strength. By having massive amount of tunable parameters, the are exceptional at "fitting" to data. This is a gift, a curse and something that we must constantly try to balance, With enough eurons, model can easily memorize a dataset; however, it can not generalize the data with to few. This is one reason why we do not simply solve problems with neural networks by using the most neuron or biest models posibble.

**Overfiting** is effectively just memorizing the data without any understanding of it. An overfit model will do very well predicting the data that it has already seen, but often significantly worse on unseed data.

Without knowing if a model overfits the training data, we cannot trust the model's result.To get _generalize model_, it essential to have both **training** and **testing data** as seperate sets for different purpose.

1. **Training** should only be used to train a model. 
2. **Testing** data should only be used to validate a model's performance after training 

One option to prevent overfitting is to change the model's size. If a models is not learning at all, one sulition might be to try a larger model. If your model is learning, but there's a divergence between the training and testing data, it could mean that rou should try a smaller model.

One general rule to follow when selecting initial model hyperparameters is to find the smalles model possible ways to avoid overfitting are regularization techniques we'll dicuss in chapter 14, and the Dropout layer explained in chapter 15. 

Often divergence of the training and testing data can take a long time to occur. The process of tring different model settings is called hyperparameter searching. Initially, you can very quickly (usually within minutes) try different settings ( layer sizes ) to see if the models are learing something.

If they are, train the model fully -- or at least significantly longer -- and compare result to pick the best set of hyperparameters. Another possibility is to create a list of different hyperparamter sets and train the model in a loop using each of those sets at a time to pick the best set at the end.

The reasoning here is that the fewer neurons can mean it's easier for neural network to generalize ( acutally learn the meaning of the data) compared to memoring the data.

**Remember** that th neural network want to decrease training loss and follows the path of least resistance to meet that objective. Our job as the programmer is to make the path generalization the easiest path. This can ofthen mean our job is acutally to make the path to lowering loss for the model more challenging!
