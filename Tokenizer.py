class Tokenizer:
    Input_list=[]
    Output_list=[]
    token_list=[]
    token_dict=[]
    special_symbols={"<":"lt;",">":"gt"}
    File_name=""
    keyword =["class","construnctor","function","method","field","static","var","int","char","boolean","void","true","false","null","this","do","if","else","while","return","let"]
    symbols = list("{}()[].,;+-*/&|<>=-~+-*/&|<>=")
    def read_lines(file_name):
        Tokenizer.File_name = file_name
        with open(file_name,'r') as input_file:
            Line_List = input_file.readlines()
            #print(Line_List)
            i=0
            Line = Line_List[0].strip()
            while i<len(Line_List):
               Line=Line_List[i].strip()
               if(Line==""):
                   i+=1
                   Line=Line_List[i].strip()
                   continue
               elif(Line.find("//")!=-1 and Line[0:2]=="//"):
                   i+=1
                   Line = Line_List[i].strip()
                   continue
               elif(Line.find("//")!=-1):
                   Line=Line[0:Line.index("//")].strip()
                   Tokenizer.Input_list.append(Line)
                   i+=1
               elif(Line.find("/*")!=-1):
                   i=i+1
                   while(Line.find("*/")==-1):
                      Line = Line_List[i].strip()
                      if(Line.find("/*")!=-1):
                         break
                      i=i+1
               else:
                   Tokenizer.Input_list.append(Line)
                   i=i+1
        Tokenizer.add_tokens()
    def write_file(self=None):
        Write_file = Tokenizer.File_name.split(".")[0]+"T.xml"
        with open(Write_file,"w") as file:
            file.write("<tokens>"+"\n")
            file.flush()
            for i in Tokenizer.token_dict:
                file.write(i+"\n")
                file.flush()
            file.write("</tokens>"+"\n")
            file.flush()
    def add_tokens(self=None):
        for i in Tokenizer.Input_list:
            current_token=""
            Character_list = list(i)
            current_token=""
            a=0
            while a<len(Character_list):
                if(Character_list[a]==" "):
                    Tokenizer.Output_list.append(current_token)
                    current_token=""
                    a=a+1
                elif(Character_list[a]=="\""):
                    current_token+=Character_list[a]
                    a=a+1
                    while(Character_list[a]!="\""):
                        current_token+=Character_list[a]
                        a+=1
                    current_token+=Character_list[a]
                    Tokenizer.Output_list.append(current_token)
                    current_token=""
                    a+=1
                elif(Character_list[a] in (Tokenizer.symbols)):
                    if(current_token==""):
                        Tokenizer.Output_list.append(Character_list[a])
                        a+=1
                    else:
                        Tokenizer.Output_list.append(current_token)
                        Tokenizer.Output_list.append(Character_list[a])
                        current_token=""
                        a+=1
                else:
                    current_token+=Character_list[a]
                    a=a+1
        Tokenizer.token_list=filter(None,Tokenizer.Output_list)
        Tokenizer.add_token_type()
    def token_type(token,self=None):
        if(token in Tokenizer.symbols):
            return "symbol"
        elif(token in Tokenizer.keyword):
            return "keyword"
        elif(token.find("'")!=-1):
            return "char"
        elif(token.find('"')!=-1):
            return "stringConstant"
        elif(token.isdigit()):
            return "integerConstant"
        else:
            return "identifier"
    def add_token_type(self=None):
        for i in Tokenizer.token_list:
            if(i.find("\"")!=-1):
               Tokenizer.token_dict.append("<"+Tokenizer.token_type(i)+"> "+i.replace("\"","")+" </"+Tokenizer.token_type(i)+">")
               continue
            elif (i.find("<")!=-1):
               Tokenizer.token_dict.append("<"+Tokenizer.token_type(i)+"> "+"&lt;"+" </"+Tokenizer.token_type(i)+">")
               continue
            elif (i.find(">")!=-1):
               Tokenizer.token_dict.append("<"+Tokenizer.token_type(i)+"> "+"&gt;"+" </"+Tokenizer.token_type(i)+">")
               continue
            elif (i.find("&")!=-1):
               Tokenizer.token_dict.append("<"+Tokenizer.token_type(i)+"> "+"&amp;"+" </"+Tokenizer.token_type(i)+">")
               continue    
            Tokenizer.token_dict.append("<"+Tokenizer.token_type(i)+"> "+i+" </"+Tokenizer.token_type(i)+">")
        Tokenizer.write_file()
    def out_putfile(self=None):
        return Tokenizer.File_name.split(".")[0]+"T.xml"















