class animal:
    def __init__(self, height,heavy,sex,move): 
        self.height = height
        self.heavy = heavy
        self.move = move 
        self.sex = sex
    
Lion = animal("3ft","700kg","female"," are running")
Lion.type = "Lion"
Bird = animal("25cm","10kg","male"," are flying")
Bird.type = "Bird"
print(Lion.sex + " " +Lion.type + Lion.move) 
