a = '''
OOOOOOO
O-----O
O->-\-O
O-----O
O---#-O
O-----O
OOOOOOO
'''
my_list =  [(list(map(str,i))) for i in a.split()]   

out_Counter=-1
in_counter = 0
breaking= False
while breaking ==False:
    for x in range(len(my_list)):
        if breaking==False:
            out_Counter+=1
        else:
            break;
        for y in range(len(my_list[x])):
            in_counter+=1
            if  my_list[x][y]== ">":
                real_index = my_list[x].index(">")
                
                breaking=True;
                break;
        
            
    print(out_Counter,real_index)