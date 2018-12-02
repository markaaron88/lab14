def Suess():
  file_object = open("C:\Users\maris\Desktop\Lab14\eggs.txt","r")
  text = file_object.read()
  file_object.close()


  textfiles = text.lower().replace("-"," ").split()
  uniqueWordCount = 0
  count = {}

  for word in textfiles:
   if word in count:
     count[word] += 1
   else:
     count[word] = 1
   
  final = sorted(count.iteritems(), key = lambda x: x[1], reverse = True)
  
  print 'The count of how often each of the words appears is:'
  print  len(count)
  print '\nPrint out the total distinct count and the count for each of the words:'
  print final
  print '\n Tne most commonly occuring word in the book:'
  return final[0]
  
  
  
  
  
  