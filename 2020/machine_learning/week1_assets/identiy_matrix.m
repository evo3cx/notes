% Initializ random matrices A and B
A = [1,2; 4,5]
B = [1,1;0,2]

% Initialize a 2 by 2 identity matrix
I = eye(2)

% The above notation is the same as I = [1,0;0,1]

% What happens when we multiply I * A?
IA = I *A

AI = A * I

% Compute A * B
AB = A * B

% Is it qual to B *A
BA = B*A