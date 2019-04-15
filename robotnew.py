class robot:
    def __init__(self,name,color,language,mobile):
        self.name=name
        self.color=color
        self.language=language
        self.mobile=mobile
    def __str__(self):
        rep = "Robot object\n"
        rep += "\n name: <"+ self.name + ">,|color: <" + self.color + "> |language <" + self.language + "> |mobile? <" + self.mobile + ">\n"
        return rep  
    def introduce_self(self):
        print("\n My name is <", self.name, ">, I am <", self.color, ">, and I speak <", self.language, ">, and I am mobile? <",self.mobile,">\n")

Tom=robot("Tom","#008000","Español","True")
Tom.introduce_self()
print(Tom)
Mary=robot("Mary","#ff6700","Français","False")
Mary.introduce_self()
print(Mary)
