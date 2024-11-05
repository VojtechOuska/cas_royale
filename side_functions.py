class Cookie:
    def __init__(self):
        pass
    
    def cookie_function(self):
       
        with open("side", mode="r")as side:
            cookie_list=[]
            p_side=side.readlines()
            
            for one_part in p_side:
            
                cookie_list.append(one_part)
            if len(cookie_list)<1:
                return True
                


            else:
                return False
        with open("side", mode="w")as side:
            side.write("dalsi navsteva")
 
    
    
    