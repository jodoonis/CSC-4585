# Workshop #1: Concolic Testing
___

#### _Code_
```sh
def buggyFunc(float_var, int_var):
    res = []
    temp_var = int(float_var)
    if (temp_var == 3 * int_var):
        if (int_var > temp_var - 50):
            print(res[5])
```
## _Concrete_
### c == 3*b
>a=5.1, b=15, c=5

5 == 3*15
5 == 45 
FALSE

> a=60.15, b=20, c=60

60 == 3*20
60 == 60
TRUE
___

### b > c - 50 
>a=60.15, b=20, c=60

20 > 60 - 50
20 > 10
TRUE
___


## _Values_
| Symbolic              | Path Constraints |
|-----------------------|------------------|
| float_var = a         | c == 3b          |
| int_var = b           | b > c - 50       |
| temp_var = int(a) = c | a < 75           |
|                       | b < 25           |