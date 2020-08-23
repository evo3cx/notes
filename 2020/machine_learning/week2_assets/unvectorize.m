% Uvectorized implementation

function prediction = unvectorize(theta, x)
  
  prediction = 0.0;
  
  % number of dataset
  n = size(x,1);
  
  for j = 1:n,
    prediction = prediction + theta(j) * x(j)
  end;
  
 endfunction