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


