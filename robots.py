class robot:
    def __init__(self,name,color,language):
        self.name=name
        self.color=color
        self.language=language
    def introduce_self(self):
       print("\n My name is <", self.name, ">, I am <", self.color, ">, and I speak <", self.language, ">\n")

Tom=robot("Tom","#008000","Español")
Tom.introduce_self()
Mary=robot("Mary","#ff6700","Français")
Mary.introduce_self()
