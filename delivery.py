class Delivery(Registration,Invoice, Tools):
    
    def __init__(self):
        super().__init__()
        self.totaldelivery=0
        self.avialabledeliveries=6
    def action(self):
        if self.check_location():
            self.totaldelivery +=1
            self.avialabledeliveries -=1
        else:
            print("sorry,Delivery not available outside valley!")
    def check_location(self):
        if self.out_valley==False:
            return True
    def update_invoice(self):
       # database.update()
        name_of_tool = self.tool_name
        username = self.username
        invoice_no = self.invoice_no
        
        

    
