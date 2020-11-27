# pyfuzzysystem
Implementation of a fuzzy inference system

## Requirements 📋
This project was developed using `python3.7.4`.

To install the `python` dependencies use:
```bash
make install
```

## Usage ⚙️
To create fuzzy variables use:
```python
my_var = FuzzyVariable('my_var')\
    .add('bad',  Triangular(3, 6, 7))\
    .add('good', Gamma(5, 10))\
    .add('excelent', Gaussian(8, 15))

second_var = FuzzyVariable('second_var')\
    .add('low',  S(1, 2))\
    .add('high', Z(3, 4))
```
> See `membershhip` submodule for details about membership functions

To create fuzzy systems use:
```python
system = LarsenSystem(centroid)
system += (my_var['bad']) >> +second_var['low']
system += (my_var['good'] | my_var['excelent']) >> +second_var['high']
```
> See `system` submodule for details about the implemented systens.
> Also check `defusification` submodule for more defuzification functions
 
To use the system:
```python
input = {'my_var':8, 'second_var':1.5}
output = system.infer(input)
print(output)
```

## Autores ✒️

- **Lazaro Raul** - [stdevRulo](https://github.com/stdevRulo)

## Licencia 📄

This project is under the License (MIT License) - see the file [LICENSE.md](LICENSE.md) for details.

## More

For details about the implementation read the [doc](doc/Informe.pdf)