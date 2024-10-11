# clase Mates con métodos estáticos

class Mates:
    
    @staticmethod
    def mayor(a, b):
        if a > b:
            return a
        else:
            return b
        
    @staticmethod
    def producto(a, b, c):
        return a * b * c
    
    @staticmethod
    def potencia(base, exponente):
        return base ** exponente