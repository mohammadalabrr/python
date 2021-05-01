def create_spend_chart(categories):
  cates = []
  spending = []
  spent = 0
  #Creates a list of category names + spending per category
  for category in categories:
    cates.append(category.cate)
    for item in category.ledger:
      spent = 0
      if item["amount"] < 0:
        spent += int(item["amount"])
    spending.append(spent)
  total = sum(spending)
  #Changes amounts in spending to percents
  for num in spending:
    spending[spending.index(num)] = int((num / total) * 10) * 10
  #Length of longest string in cates
  longest = len(max(cates, key=len))  
  #Starts putting together output strings
  title = "Percentage spent by category" + "\n"
  #Sets length of each category to max
  for cate in cates:
    cates[cates.index(cate)] = cate.ljust(longest)
  #Prints all categories in a vertical line
  cateString = "     "
  for i in range(0, longest):
    for cate in cates:
      cateString += cate[i] + "  " #Two spaces between each category
    cateString += "\n     " #Categories start 5 spaces away from edge
  graph = ""
  for i in range(100, -10, -10):
    bar = " "
    line = str(i).rjust(3) + "|"
    #Add o if percent spending reaches there, spaces otherwise
    for percent in spending:
      if percent >= i:
        bar += "o  "
      else:
        bar += "   "
    line += bar
    graph += line + "\n"
    dashes = "    " + (len(cates) * 3) * "-" + "-" +  "\n"
    output = title + graph + dashes + cateString
  return(output)
