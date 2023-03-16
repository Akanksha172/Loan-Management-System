import pymysql as pm

class Connection:
    def __init__(self):
        self.con = pm.connect(host='localhost',user='root',password='MYSQLPiCT@123',database='try')
        self.cursor = self.con.cursor()
    
    def storeUser(self,oname,oscore,oemail,opass1):
        # print("***********hello*****************")
        sql="insert into customer (name,cibil_score,email,password) values ('%s','%d','%s','%s')" %(oname,oscore,oemail,opass1)
        self.cursor.execute(sql)
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback() 
            self.status=False
        return self.status

    def StoreDetails(self,oamt,ocoll,orate,otype,oemail,oagent):
        sql="insert into loaninfo (amt,collateral_val,type,interest_rate,email,agent_info) values ('%d','%d','%s','%d','%s','%s')" %(oamt,ocoll,otype,orate,oemail,oagent)
        self.cursor.execute(sql)
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback() 
            self.status=False
        return self.status
        


    def checkuser(self,email):
        sql="select * from customer where email = '%s'" % (email)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status


    def checkUser(self,email,pass1):
        sql="select * from customer where email = '%s' and password = '%s' " % (email,pass1)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status
    
    def checkAgent(self,email,pass1):
        sql = "select * from agent where username = '%s' and password = '%s' " % (email,pass1)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status


    def checkManager(self,email,pass1):
        sql = "select * from managerinfo where manager_id = '%s' and password = '%s' " % (email,pass1)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status
        

    def acno(self,email):
        sql="select acno from account where email ='%s'"%(email)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getAgentid(self,mail):
        sql = "select emp_id from loanagent where email = '%s'" % (mail)
        self.cursor.execute(sql)
        self.id = self.cursor.fetchall()
        return self.id

    def verifyuser_agent(self,mail):
        sql = "select agent_id from loaninfo where email = '%s'" % (mail)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status
    
    def getallloaninfo(self,mail,id):
        sql = "select * from loaninfo where email = '%s' and loan_id = '%d' " % (mail,id)
        self.cursor.execute(sql)
        self.hoil = []
        self.hoil = self.cursor.fetchone()
        print(self.hoil)
        return self.hoil


    def getallloaninfo1(self,mail,id):
        print(mail)
        print(id)
        print(type(id))
        sql = "select * from acc_loans where email = '%s' and loan_id = '%d' " % (mail,id)
        self.cursor.execute(sql)
        self.hoil = []
        self.hoil = self.cursor.fetchone()
        print(self.hoil)
        return self.hoil


    def acceptedloans(self,mail,aid,lid):
        sql = "select * from loaninfo where email = '%s' and loan_id  = '%d'" % (mail,lid)
        self.cursor.execute(sql)
        self.hoil = []
        self.hoil = self.cursor.fetchone()
        print(self.hoil)
        sql1 = "insert into acc_loans(loan_id,type,interest_rate,amt,collateral_val,email,agent_id) values('%d' , '%s', '%d' ,'%d', '%d' ,'%s','%s')"%(self.hoil[0],self.hoil[2],self.hoil[3],self.hoil[1],self.hoil[4],self.hoil[5],aid)
        self.cursor.execute(sql1)
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback() 
            self.status=False
        return self.status
    
    def manageracceptedloans(self,mail,lid):
        sql = "select * from acc_loans where email = '%s' and loan_id  = '%d'" % (mail,lid)
        self.cursor.execute(sql)
        self.hoil = []
        self.hoil = self.cursor.fetchone()
        print(self.hoil)
        sql1 = "insert into final_acc_loans(loan_id,type,interest_rate,amt,collateral_val,email,agent_id) values('%d' , '%s', '%d' ,'%d', '%d' ,'%s','%s')"%(self.hoil[5],self.hoil[1],self.hoil[0],self.hoil[2],self.hoil[3],self.hoil[4],self.hoil[6])
        self.cursor.execute(sql1)
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback() 
            self.status=False
        return self.status


    def getstatus(self,mail):
        sql = "select * from final_acc_loans where email = '%s' "% (mail)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status

    def verifyagent_customer(self,mail,aid):
        sql = "select * from loaninfo where email = '%s' and agent_info = '%s'"%(mail,aid)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status