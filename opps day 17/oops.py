#bank 01
bankname='sbi'
branch='chennai'        
ifsc=123456789
#
def bank_ifsc_correct():
    print("account is correct branch dtected")

def bank_ifsc_incorrect():
    print("account is incorrect branch not detected")

#bank 02
bankname='hdfc'
branch='chennai'
ifsc=987654321

def bank_ifsc_correct():
    print("account is correct branch dtected")
def bank_ifsc_incorrect():
    print("account is incorrect branch not detected")



class bank:
    bankname='sbi'
    branch='chennai'        
    ifsc=123456789
    def bank_ifsc_correct():
        print("account is correct branch dtected")
    def bank_ifsc_incorrect():
        print("account is incorrect branch not detected")

bank1=bank()
print(bank1.bankname,bank1.branch,bank1.ifsc)
cast1=bank('vidhyabathi k',11111111,'savings',10000,'chennai')
