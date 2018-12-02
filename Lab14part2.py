def Foothill():
  file_object = open("C:/Users/maris/Desktop/HTML/foothills.html","r")
  text = file_object.read()
  file_object.close()
  return text
