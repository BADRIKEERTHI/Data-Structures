class Emp:
    def dtls(self,n,i):
        self.name=n
        self.id=i
    def dsply(self):
        print(self.name,self.id)

e1=Emp()
e1.dtls("keerthi",1160)
e1.dsply()

e2=Emp()
e2.dtls("badri",1111)
e2.dsply()