# Vector Norm

pada Machine Learning ada 3 cara umum yang digunakan untuk menghitung magnitude and length dari vector.

## Vector L1 Norm

Teknik ini menghitung sum/total absolute value dari vector

rumus
```
||v||1 = |a1| + |a2| + |a3|
```

python

```python
import numpy  as np
from numpy import linalg 

a = np.array([1,2,3])
print (a)

l1 = linalg.norm(a, 1)
print (a)
```

output:
```shell
[1,2,3]

6
```

## Vector L2 Norm

Panjang vector dapat dihitung menggunakan L2 norm, dimana rumus Vector L2 adalah `L^2`

L2 norm menghitung sebagai square root dari total squared vector values dan L2 norm lebih umum digunakan pada machine learning dari pada norm yng lain.

`||v||2 = sqrt(a1^2 + a2^2 + a2^2)`

python

```python
import numpy  as np
from numpy import linalg 

a = np.array([1,2,3])
print (a)

l2 = linalg.norm(a, 2)
print (l2)
```

output:
```shell
[1,2,3]

3.741
```

## Vector Max Norm

Panjang vector dapat dihitung menggunakan the maximum norm, also called max norm.

rumus:
`maxnorm(v) = ||v||inf`

dimana max norm mengembalikan maximum value dari vector, atau dapat disederhanakan
```
||v||inf = max(|a1|, |a2|, |a3|)
```

python
```python

import numpy  as np
from numpy import linalg 

a = np.array([1,2,3])
print (a)

maxnorm = linalg.norm(a, np.inf)
print (maxnorm)
```

output:
```shell
[1,2,3]

3
```

max norm digunakan untuk regulazation in machine learning seperti neural network weight 