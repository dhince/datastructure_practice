#list = [1,2,3,4,5,6]
#print(list[len(list) - 1])

def FindSum(list):
  if len(list) == 1:
    return list[0]
  last_value = list.pop()
  sum = FindSum(list) + last_value
  return sum

if __name__ == "__main__":
    list = [1,2,3,4,5]
    sum = FindSum(list)
    print(sum)