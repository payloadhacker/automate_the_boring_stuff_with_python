
def comma(item):
        if not item:
              return " " 
        for i in str(len(item)):
            if len(item) == 1:
                  return str(item[0])
            return(", ".join(item[:-1]) + ', and ' + item[-1])
        # return ", and".join(str(spam)) )
            

result= comma(["y"])
print(result)
# 
