#------------------------------------------------------------------------------
#purpose:
#get only n-gram frequency from the text
#
#author:cuixiaofei          time:205.7.9
#------------------------------------------------------------------------------

class NGram(object):
    def __init__(self,text,n=3):
        self.n = n
        self.table = {}
        self.parse_text(text)

    def parse_text(self,text):
        chars = ' '*self.n
        #initial sequence of spaces with length n
        i = 0
        for letter in ("".join(text.split())):
            chars = chars[1:] + letter
            i = i + 1
            #append letter to sequence of length n
            if i < self.n:
                continue
            self.table[chars] = self.table.get(chars,0) + 1
            #increment count



