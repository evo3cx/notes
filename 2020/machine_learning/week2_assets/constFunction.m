function j = constFunction(X, y, theta)
  % Cost Function J
  % https://www.coursera.org/learn/machine-learning/lecture/LRQnl/control-statements-for-while-if-statement

  
  % X is the design matrix containing our training examples.
  % y is the class labels
  
  % Number of training examples
  noTrainingExample = size(X, 1); 
  
  % Predictions of hypothesis on all no of training examples
  predictions = X*theta;
  
  display(predictions);
  
  % squared errors
  sqrErrors = (predictions-y).^2;
  
  display(sqrErrors);
  j = 1/( 2* noTrainingExample ) * sum(sqrErrors);
 