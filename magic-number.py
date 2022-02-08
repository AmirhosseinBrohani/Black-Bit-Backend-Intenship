class Strint(int):
    
    def __lt__(self, other):
        self = str(self)
        other = str(other)
        if int(self[-1]) < int(other[-1]) :
            return True
        return False    

    def __gt__(self, other):
        self = str(self)
        other = str(other)
        if int(self[-1]) > int(other[-1]) :
            return True
        return False    

    def __le__(self, other):
        self = str(self)
        other = str(other)
        if int(self[-1]) <= int(other[-1]) :
            return True
        return False    

    def __ge__(self, other):
        self = str(self)
        other = str(other)
        if int(self[-1]) >= int(other[-1]) :
            return True
        return False    

    def __eq__(self, other):
        self = str(self)
        other = str(other)
        if int(self[-1]) == int(other[-1]) :
            return True
        return False    

    def __ne__(self, other):
        self = str(self)
        other = str(other)
        if int(slef[-1]) != int(other[-1]) :
            return True
        return False    

    def __add__(self, other):
        self = str(self)
        other = str(other)
        self = self + other 
        return self
        

    def __sub__(self, other):
        self = str(self)
        other = str(other)
        if self.endswith(other):
            self = self[:-(len(other))]
            if result:
                return int(self)
            return 0
        raise Exception('The subtraction is not valid!')

    def __len__(self):
        self = str(self)
        first_finder = 0
        length = 0
        for i in range(len(self)) :
            first_finder += int(self[i])
            if first_finder >= 0 :
                length += 1 
        return length        

    def __call__(self):
        self = str(self)
        change_dictionary = {
            '0': '۰',
            '1': '۱',
            '2': '۲',
            '3': '۳',
            '4': '۴',
            '5': '۵',
            '6': '۶',
            '7': '۷',
            '8': '۸',
            '9': '۹'
        }
        res = ""
        for i in self :
            res += change_dictionary[i]
        return res    
        return result
