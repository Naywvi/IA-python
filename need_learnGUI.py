
import json

from tkinter import *


class learn:
    def __init__(self):
        self.dataJ = json.loads(open('intents.json').read())
        self.dictionnary = self.selectIntents()
        self.tag = self.selectField('tag')
        self.patterns = self.selectField('patterns')
        self.Response = self.selectField('responses')
        self.Context = self.selectField('context')

    def selectIntents(self):
        documents = []
        for intent in self.dataJ['intents']:
            documents.append(intent)
        return documents
        
    def selectField(self,field):
        documents = []
        for intent in self.dataJ['intents']:
            while intent[field]:
                documents.append(intent[field])
                break
        return documents


root = Tk()
def getResponse():
    response = "".join(learn().tag[0])
    txt.insert(END, "\n" +  "NayB :" + response)


def send():
    send = "Moi :" +e.get()
    txt.insert(END, "\n" + send)
    e.delete(0,END)
    getResponse()

txt = Text(root)
txt.grid(row=0,column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1,column=0)
envoyer = Button(root,text="Envoyer", command=send).grid(row=1,column=1)
root.title("NayBLearn")




learn()
root.mainloop()




