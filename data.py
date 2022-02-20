import os,re;from datetime import datetime
try:
    import autocorrect
except:
    os.popen('pip install autocorrect')

class Root:
    def __init__(self):
        self.child={}
        self.data=False

def AddNode(getInput,parent):
    for y in getInput:
        if y not in parent.child:
           parent.child[y]=Root()
        parent.child[y]                                                                     parent.data=True
def Search(searchval,setvalue,root):
    corrector=autocorrect.Speller()
    correctvalue=corrector(searchval)

    if searchval != correctvalue:
        print("[*] Suggestion => %s" % correctvalue)
    else:
        temp,xx="",root
        def Repeat(kbx,xx):
            for c in range(0,len(searchval)):
                if searchval[c] == ".":
                    for yk in xx.child:
                        global temp
                        Repeat(c+1,xx)
                        temp+=yk
                else:
                    if searchval[c] not in xx.child:
                        return False
                    else:
                        xx=xx.child[c]
                        temp+=xx
                print(temp)
            return xx.data
        Repeat(None,xx)

class Dictionary:
    def __init__(self):
        reader=open(os.getcwd()+"/list.txt",'r')
        self.newset=set()
        self.parent=Root()
        for i in reader.readlines():
            k=str(i).replace("\n","")
            AddNode(k,self.parent)
            self.newset.add(k)

    def Operation(self):
        print("1. Show Data Dictionary")
        print("2. Insert Word in Dictionary")
        print("3. Search Word")
        print("4. Quit")
        while True:
            try:
                getInput=input("Enter the choice:  ")
                if int(getInput) == 1:
                    old_t=datetime.now()
                    print(self.parent.child.keys())
                    print("query time: ",datetime.now()-old_t)
                elif int(getInput) ==4:
                    break
                elif int(getInput) == 2:
                    getvalue=input("Enter the  word to insert:  ")
                    print(AddNode(str(getvalue),self.parent))

                elif int(getInput)==3:
                    searchValue=input("Word to Search: ")
                    Search(str(searchValue),self.newset,self.parent)
            except  Exception as e:
                print("Invalid Choice")

if __name__ == "__main__":
    DicObj=Dictionary()
    DicObj.Operation()
