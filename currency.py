# Currency

class Currency:
    
    def __init__(self,value,code):
        self.value = value
        self.code = code.upper()
        
    def __str__(self):
        return f'{self.value:.2f} {self.code}'
    
    def __eq__(self, rhs):
        if self.code == rhs.code and self.value == rhs.value:
            return True
        return False
    
    def __gt__(self,rhs):
        if self.code == rhs.code:
            return self.value > rhs.value
        raise ValueError('Moedas devem ser do mesmo codigo.')
    
    def __ge__(self,rhs):
        return (self > rhs) or (self == rhs)  


if __name__ == '__main__':
    moeda1 = Currency(50,'BRl')
    moeda2 = Currency(50, 'BRL')
    print(moeda1 >= moeda2)