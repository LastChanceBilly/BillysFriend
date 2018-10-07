import wikipedia

class WikiSearch:
    def __init__(self, lines, lang):
        self.lines = lines
        self.lang = lang
        wikipedia.set_lang(lang) 

    def getContent(self, index):
        try:
            msg = wikipedia.summary(index, sentences=self.lines)
            return msg
        except wikipedia.exceptions.PageError:
            suggs = (' ')
            suggs = wikipedia.suggest(index)
            print(suggs)
            msg=' '

            if(suggs != None):
                msg="\nMaybe you could try \n" + suggs 
            return "I couldn't find any info about "+ index +"..."+msg
        except wikipedia.exceptions.DisambiguationError as e:
            return e
        except wikipedia.exceptions.PageError as e:
            print(e)
            return(" ")

    def changeLang(self, lang):
        wikipedia.set_lang(lang)
        try:
            data = wikipedia.search("Day")
            if(len(data) > 0):
                return("Languaje set to "+ lang)
        except Exception:
            wikipedia.set_lang(self.lang)
            return("Couldn't cet languaje to "+ lang +", changing it back to "+ self.lang)