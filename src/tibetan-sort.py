# coding=UTF-8
class TibetanSort():
    def __init__(self):
        self.trie = None

    def init(self):
        self.trie = {}
        self.addBatch(['ཀ', 'ྈྐ', 'ཫ', 'དཀ', 'བཀ', 'རྐ', 'ལྐ', 'སྐ', 'བརྐ', 'བསྐ'])
        self.addBatch(['ཁ', 'ྈྑ', 'མཁ', 'འཁ'])
        self.addBatch(
            ['ག', 'དགག', 'དགང', 'དགད', 'དགན', 'དགབ', 'དགཝ', 'དགའ', 'དགར', 'དགལ', 'དགས', 'དགི', 'དགུ', 'དགེ', 'དགོ',
             'དགྭ', 'དགྱ', 'དགྲ', 'བགག', 'བགང', 'བགད', 'བགབ', 'བགམ', 'བགཾ', 'བགཝ', 'བགའ', 'བགར', 'བགལ', 'བགི',
             'བགུ', 'བགེ', 'བགོ', 'བགྭ', 'བགྱ', 'བགྲ', 'བགླ', 'མགག', 'མགང', 'མགད', 'མགབ', 'མགའ', 'མགར', 'མགལ',
             'མགི', 'མགུ', 'མགེ', 'མགོ', 'མགྭ', 'མགྱ', 'མགྲ', 'འགག', 'འགང', 'འགད', 'འགན', 'འགབ', 'འགམ', 'འགཾ',
             'འགའ', 'འགར', 'འགལ', 'འགས', 'འགི', 'འགུ', 'འགེ', 'འགོ', 'འགྭ', 'འགྱ', 'འགྲ', 'རྒ', 'ལྒ', 'སྒ', 'བརྒ',
             'བསྒ'])
        self.addBatch(
            ['ང', 'ྂ', 'ྃ', 'དངག', 'དངང', 'དངད', 'དངན', 'དངབ', 'དངའ', 'དངར', 'དངལ', 'དངི', 'དངུ', 'དངེ', 'དངོ', 'མངག',
             'མངང', 'མངད', 'མངན', 'མངབ', 'མངའ', 'མངར', 'མངལ', 'མངི', 'མངུ', 'མངེ', 'མངོ', 'རྔ', 'ལྔ', 'སྔ', 'བརྔ',
             'བསྔ'])
        self.addBatch(['ཅ', 'གཅ', 'བཅ', 'ལྕ', 'བལྕ'])
        self.addBatch(['ཆ', 'མཆ', 'འཆ'])
        self.addBatch(['ཇ', 'མཇ', 'འཇ', 'རྗ', 'ལྗ', 'བརྗ'])
        self.addBatch(['ཉ', 'ྋྙ', 'གཉ', 'མཉ', 'རྙ', 'ཪྙ', 'སྙ', 'བཪྙ', 'བརྙ', 'བསྙ'])
        self.addBatch(['ཏ', 'ཊ', 'ཏྭ', 'ཏྲ', 'གཏ', 'བཏ', 'རྟ', 'ལྟ', 'སྟ', 'བརྟ', 'བལྟ', 'བསྟ'])
        self.addBatch(['ཐ', 'ཋ', 'མཐ', 'འཐ'])
        self.addBatch(
            ['ད', 'ཌ', 'གདག', 'གདང', 'གདད', 'གདན', 'གདབ', 'གདམ', 'གདཾ', 'གདའ', 'གདར', 'གདལ', 'གདས', 'གདི', 'གདུ', 'གདེ',
             'གདོ', 'གདྭ', 'བདག', 'བདང', 'བདད', 'བདབ', 'བདམ', 'བདཾ', 'བདའ', 'བདར', 'བདལ', 'བདས', 'བདི', 'བདུ', 'བདེ',
             'བདོ', 'བདྭ', 'མདག', 'མདང', 'མདད', 'མདན', 'མདབ', 'མདའ', 'མདར', 'མདལ', 'མདས', 'མདི', 'མདུ', 'མདེ', 'མདོ',
             'མདྭ', 'འདག', 'འདང', 'འདད', 'འདན', 'འདབ', 'འདམ', 'འདཾ', 'འདཝ', 'འདའ', 'འདར', 'འདལ', 'འདས', 'འདི', 'འདུ',
             'འདེ', 'འདོ', 'འདྭ', 'འདྲ', 'རྡ', 'ལྡ', 'སྡ', 'བརྡ', 'བལྡ', 'བསྡ'])
        self.addBatch(
            ['ན', 'ཎ', 'གནག', 'གནང', 'གནད', 'གནན', 'གནབ', 'གནམ', 'གནཾ', 'གནཝ', 'གནའ', 'གནར', 'གནལ', 'གནས', 'གནི', 'གནུ',
             'གནེ', 'གནོ', 'གནྭ', 'མནག', 'མནང', 'མནད', 'མནན', 'མནབ', 'མནམ', 'མནཾ', 'མནའ', 'མནར', 'མནལ', 'མནས', 'མནི',
             'མནུ', 'མནེ', 'མནོ', 'མནྭ', 'རྣ', 'སྣ', 'བརྣ', 'བསྣ'])
        self.addBatch(
            ['པ', 'ྉྤ', 'དཔག', 'དཔང', 'དཔད', 'དཔབ', 'དཔའ', 'དཔར', 'དཔལ', 'དཔས', 'དཔི', 'དཔུ', 'དཔེ', 'དཔོ', 'དཔྱ',
             'དཔྲ', 'ལྤ', 'སྤ'])
        self.addBatch(['ཕ', 'ྉྥ', 'འཕ'])
        self.addBatch(
            ['བ', 'དབག', 'དབང', 'དབད', 'དབན', 'དབབ', 'དབའ', 'དབར', 'དབལ', 'དབས', 'དབི', 'དབུ', 'དབེ', 'དབོ', 'དབྱ',
             'དབྲ', 'འབག', 'འབང', 'འབད', 'འབན', 'འབབ', 'འབམ', 'འབཾ', 'འབའ', 'འབར', 'འབལ', 'འབས', 'འབི', 'འབུ',
             'འབེ', 'འབོ', 'འབྱ', 'འབྲ', 'རྦ', 'ལྦ', 'སྦ'])
        self.addBatch(
            ['མ', 'ཾ', 'དམག', 'དམང', 'དམད', 'དམན', 'དམབ', 'དམཝ', 'དམའ', 'དམར', 'དམལ', 'དམས', 'དམི', 'དམུ', 'དམེ', 'དམོ',
             'དམྭ', 'དམྱ', 'རྨ', 'སྨ'])
        self.addBatch(['ཙ', 'གཙ', 'བཙ', 'རྩ', 'སྩ', 'བརྩ', 'བསྩ'])
        self.addBatch(['ཚ', 'མཚ', 'འཚ'])
        self.addBatch(['ཛ', 'མཛ', 'འཛ', 'རྫ', 'བརྫ'])
        self.addBatch(['ཞ', 'གཞ', 'བཞ'])
        self.addBatch(['ཟ', 'གཟ', 'བཟ'])
        self.addBatch(['ཞ', 'གཞ', 'བཞ'])
        self.addBatch(['ཡ', 'གཡ'])
        self.addBatch(['ར', 'ཪ', 'ཬ', 'བརླ', 'བཪླ'])
        self.addBatch(['ཤ', 'ཥ', 'གཤ', 'བཤ'])
        self.addBatch(
            ['ས', 'གསག', 'གསང', 'གསད', 'གསན', 'གསབ', 'གསའ', 'གསར', 'གསལ', 'གསས', 'གསི', 'གསུ', 'གསེ', 'གསོ', 'གསྭ',
             'བསག', 'བསང', 'བསད', 'བསབ', 'བསམ', 'བསཾ', 'བསའ', 'བསར', 'བསལ', 'བསས', 'བསི', 'བསུ', 'བསེ', 'བསོ',
             'བསྭ', 'བསྲ', 'བསླ'])
        self.addBatch(['ཧ', 'ལྷ'])
        self.addBatch(['ཱ', 'ི', 'ཱི', 'ྀ', 'ཱྀ', 'ུ', 'ཱུ', 'ེ', 'ཻ', 'ོ', 'ཽ'])
        self.addBatch(['།', '༎', '༏', '༐', '༑', '༔', '༴', '\u0F0B'])

        i, p, s = self.getLongestMatch('\u0F0B', 0)
        self.addToTrie(p, s, '\u0F0C')

    def addToTrie(self,p,s,str):
        current = self.trie
        for i in range(len(str)):
            c = str[i]
            if current.get(c) == None:
                current[c] = {}
                current = current[c]
            else:
                current = current[c]

        current["p"] = p
        current["s"] = s

    def addBatch(self,a: list):
        primary = ord(a[0][0])
        for index in range(len(a)):
            self.addToTrie(primary,index,a[index])

    def getLongestMatch(self, str, off):
        strLength=len(str)
        current = self.trie
        saveNbChars = 0
        savePrimary = 0
        saveSecondary = 0
        for i in range(off, strLength):
            curChar = str[i]
            if current.get(curChar) != None:
                current = current[curChar]
                if current.get("p") != None :
                    saveNbChars = saveNbChars + 1
                    savePrimary = current.get("p")
                    saveSecondary = current.get("s")
                elif savePrimary == 0:
                    savePrimary = ord(str[i])
                    saveNbChars = 1
            else:
                if saveNbChars == 0:
                    return 1, ord(str[i]), 0

                return saveNbChars, savePrimary, saveSecondary

        return saveNbChars, savePrimary, saveSecondary

    def compare(self, a, b):
        if self.trie == None:
            self.init()

        aOffset = 0
        bOffset =0
        i =0
        while True:
            alm_i,alm_p, alm_s = self.getLongestMatch(a, aOffset)
            blm_i, blm_p, blm_s = self.getLongestMatch(b, bOffset)

            if alm_i < 1 and blm_i < 1:
                return 0

            if alm_i < 1:
                return -1

            if blm_i < 1:
                return 1

            if alm_p < blm_p:
                return -1

            if alm_p > blm_p:
                return 1

            if alm_s < blm_s:
                return -1

            if alm_s > blm_s:
                return 1

            aOffset = aOffset + alm_i
            bOffset = bOffset + blm_i

        return 0

def main():
    sorter = TibetanSort()
    print(sorter.compare("བརྐ","ག"))
    print(sorter.compare("ག", "བ"))
    print(sorter.compare("ག་བརྐ", "ག་ག"))



if __name__ == '__main__':
    main()
