function predicton = vectorizeImpl(theta, x)
  % display(theta); transponse theta so we can use multiplication
  theta = theta';
  
  predicton = theta * x;
 endfunction