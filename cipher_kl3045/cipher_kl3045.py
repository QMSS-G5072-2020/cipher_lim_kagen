def cipher(text, shift, encrypt=True):
    """
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
    >>> cipher_kl3045.cipher('b%b', 1) #non-alphabet characters will not be processed
    'c%c'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
