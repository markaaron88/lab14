#Lab14 Mark Mariscal

def foothill():
  #Problem 2

  #Step 1. Save HTML file of website on computer completed

  #Extra Function
  
  #Step 2. Open HTML File  
  file = open
  file = open("C:/Users/maris/Desktop/HTML/foothills.html","r")
  fileText = file.read() 
  file.close()

  #Step 2. Use string processing to extract headline from paper.
  #place Headlines in Array
  headlines = [] 

  first ="&lt;h3&gt;</span>"
  second ="<span class=\"html-tag\">&lt;/h3&gt;</span>"
  
  index = 0 
  start = 0
  finish = len(fileText)
  
  while index != -1:
    index = fileText.find(first, start, finish)
    if index != -1:
      index += len(first)
    midIndex = fileText.find(second, index, finish)
    midIndex -= 1
    headlines.append(fileText[index:midIndex+1])
    start = midIndex
    
  for i in headlines:
    print(i)  
  
  

  
  
  
    









 
 
 
 
 