import itertools
class Fact:    
  

    class _Fact_iter:
        
        def __init__(self):
            self.numb = 0
            self.value = 1
        
        def __next__(self):
          
                self.numb += 1
                self.value *= self.numb
                return self.value

    def __iter__(self):
        return Fact._Fact_iter()

ft = Fact()

f = list(itertools.islice(ft,5,10))
print(f)