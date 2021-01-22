# Forward Pass

L1 regularization's penalty is the sum of all the absolte values for the weights and biases.
L2 regulatization's penalty is the sum of the squared weights and biases.

-------------------------

formula:

L1 weight regularization:

L1<sub>w</sub> = $\lambda$ $\sum$|w <sub>m</sub>|

l1 Bias regularization:

L1<sub>b</sub> = $\lambda$ $\sum$|b<sub>n</sub>|

L2 weight regularization

L2<sub>w</sub> = $\lambda$ $\sum$ w<sup>2</sup><sub>m</sub>

L2 bias regularization

L2<sub>b</sub> = $\lambda$ $\sum$ b<sup>2</sup><sub>n</sub>

Overall loss

`Loss = Dataloss + L1w + L1b + L2w + L2b` 


In python

```python

l1w = lambda_l1w * sum(abs(weigths))
l1b = lambda_l1b * sum(abs(biases))
l2w = lambda_l2w * sum(weight**2)
l2b = lambda_l2b * sum(biases**2)
loss = data_loss + l1w + l1b + l2w + l2b
```


# Backward pass (page 12)

formula:

L1 regularization:

L1<sub>w</sub> = $\lambda$ $\sum$<sub>m</sub>|w<sub>m</sub>| -> 

L'<sub>1w</sub> = ($\alpha$ $\div$ $\alpha$w<sub>m</sub>) $\lambda$ $\sum$<sub>m</sub> |w<sub>m</sub>| 

= $\lambda$ {1 : w<sub>m</sub> > 0 `or` -1: w<sub>m</sub> < 0}

```python
weights = [0.2, 0.8, -0.5]

# array of partial derivatives of L1 regularization
dL1 = []

for weight in weights:
    if weight >= 0:
        dL1.append(1)
    else:
        dL1.append(-1)

```

--------------------------------------------

L2 regularization:

L2<sub>w</sub> = $\lambda$ $\sum$w<sup>2</sup><sub>m</sub> -> 
    $\alpha$L2<sub>w</sub>$\div$$\alpha$w<sub>m</sub> 

= $\alpha$$\div$$\alpha$w<sub>m</sub>[$\lambda$ $\sum$ w<sup>2</sup><sup>m</sup>] 

= $\lambda$ ($\alpha$$\div$$\alpha$w<sub>m</sub>) w<sup>2<sup><sub>m</sub>  

= $\lambda$ * 2w<sup>2-1</sup><sub>m</sub>

= 2$\lambda$w<sub>m</sub>

This might look complicated, but is one the simpler derivative calculations that we have to derive in this book. Lambda is a constant, so we can move it outside of the derivative term. We can remove the sum operator since we calcualte the partial derivative with respect to the given paramter only and the sum of one element equals this element. So, we only need to calculate the derivative of W<sup>2</sup>, which we know is 2w. From the coding perspective, we will multiply all of the weights by 2$\lambda$. We'll implement this with NumPy directly as it's just a simple multiplication operation.
