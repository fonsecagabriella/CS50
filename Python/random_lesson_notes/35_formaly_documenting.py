# DOCSTRINGS 

""" 
Official way to comment in Python, 
doc can be generated automatically with tools 
"""



def meouw_right(n: int) -> str:
    """ 
    Meow n times. 
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A strong of n meows, one per line
    :rtype: str
    
    """
    return "meow \n" * n



number: int = int(input("Number: ")) 
meow(number)