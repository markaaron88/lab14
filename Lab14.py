def Suess():
  file_object = open("C:\Users\maris\Desktop\Lab14\eggs.txt","r")
  text = file_object.read()
  file_object.close()


  textfiles = text.lower().replace("-"," ").split()
  
  dict = dict()
  
  for word in textfiles:
    if word not in emptylist:
      dict[word] = 1
    else:
      dict[word] += 1
  return dict
   
   
  