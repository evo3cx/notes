% initialize matrix A and B

A = [1,2,4; 5,3,2]
B = [1,3,4; 1,1,1]

% initialize constant s
s = 2

% See how element-wise addition works
add_AB = A + B

% See how element-wise substraction works
sub_AB = A - B

% See how scalar multiplication works
mult_As = A * s

% Devide A by s (scalar)
div_As = A * s

% What happens if we have a Matrix + scalar?
add_As = A + s