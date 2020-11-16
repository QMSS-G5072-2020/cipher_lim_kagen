# cipher_kl3045 

![](https://github.com/kagenlim/cipher_kl3045/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/kagenlim/cipher_kl3045/branch/main/graph/badge.svg)](https://codecov.io/gh/kagenlim/cipher_kl3045) ![Release](https://github.com/kagenlim/cipher_kl3045/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/cipher_kl3045/badge/?version=latest)](https://cipher_kl3045.readthedocs.io/en/latest/?badge=latest)

Python package that contains the cipher function.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ cipher_kl3045
```

## Features

- This function can help you encrypt text, as long as the input text consists of English Alphabets.

## Dependencies

- sphinx = "^3.3.1"
- sphinxcontrib-napoleon = "^0.7"
- pytest = "^6.1.2"

## Usage

    Encrypts a given input alphabetical text string.

    Parameters (Inputs)
    ----------
    text : str
      Character input. This is the input text data, to be ciphered.
      Only uppercase or lowercase characters in the English Alphabet will be successfully ciphered.

    shift : int
      Integer input.
      Each English alphabet character will be replaced by another one.
      This parameter determines the index of alphabets that will replace the ones in the input, by providing the number
      that the alpabet will shifted by.

    encrypt : bool
      Boolean input.
      If encrypt is True (default value), each alphabet character will be replaced by another alphabet character;
      the extent of this shift will be dependent on the shift parameter.

      If encrypt is False, a similar process will happen, and the extent is also dependent on shift.
      However, when encrypt is False, it also enables decryption, if some output generated by the cipher function is
      re-entered as input into the cipher function.


    Returns (Output)
    -------
    str
      The ciphered string will be produced as output.

    Examples
    --------
    >>> import cipher_kl3045
    >>> cipher_kl3045.cipher('bob', 1) #encrypt is True by default
    'cpc'

    >>> import cipher_kl3045
    >>> cipher_kl3045.cipher('fun', 1, encrypt = False) #decryption function
    'etm'

    >>> import cipher_kl3045
    >>> cipher_kl3045.cipher('b$b', 1) #non-alphabet characters will not be processed
    'c$c'

## Documentation

The official documentation is hosted on Read the Docs: https://cipher_kl3045.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/kagenlim/cipher_kl3045/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
