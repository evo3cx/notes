function predicton = vectorizeImpl(theta, x)
  theta = theta';
  display(theta);
  predicton = theta * x;
 endfunction