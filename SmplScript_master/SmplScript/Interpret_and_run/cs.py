from os import system, name 


def cs(): 
  
    # for windows os
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux os(The name is posix)
    else: 
        _ = system('clear') 