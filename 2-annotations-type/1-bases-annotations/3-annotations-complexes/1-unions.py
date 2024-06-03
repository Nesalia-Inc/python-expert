


class Chien:
    pass 


class Chat:
    pass 



def adopter(animal : Chien | Chat) -> None:
    pass 



if __name__ == '__main__':
    medor = Chien()
    garfield = Chat()
    
    adopter(medor)
    adopter(garfield)
    