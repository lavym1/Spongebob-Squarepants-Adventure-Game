# debugger function to 
# know in code if it was meant to be a print or for debuggin
def debugger(msg):
  printNow("debugger: %d" % msg)
  

# print article takes on input named userInput
# which is an array of user inputs
def printArticle(userInput):
  article = '''After taking control of the %s 
and widening their %s in the House of Representatives 
in the recent midterm elections, Republicans are preparing 
for new %s with the Obama administration, this time over 
%s. Until now, controversial Republican-backed legislation 
rarely %s the president's desk because Senate Democrats 
%s it. Starting in January, however, Obama may have to 
decide more often whether to sign or veto %s.
Obama gave %s an early taste of veto politics recently 
when he forced congressional leaders to %s  a proposed package 
of tax breaks that were popular with many Republican constituents. 
Some Democrats did support the plan, but liberals and the White 
%s said it tilted too heavily toward %s , not %s.''' % (userInput[0], userInput[1], userInput[2], userInput[3], userInput[4], userInput[5], userInput[6], userInput[7], userInput[8], userInput[9], userInput[10], userInput[11])
  
  printNow(article)
  

#the main function call to start the madLibs
def myMadLibs():
  
  # user input array set to the max inputs needed
  userInput = [0 for i in range(12)]
  
  # collect user input to fill in the blanks
  userInput[0] = requestString("Enter a place:")
  userInput[1] = requestString("Enter a plural noun:")
  userInput[2] = requestString("Enter plural noun:")
  userInput[3] = requestString("Enter a plural noun:")
  userInput[4] = requestString("Enter a past verb:")
  userInput[5] = requestString("Enter a present verb:")
  userInput[6] = requestString("Enter a plural noun:")
  userInput[7] = requestString("Enter a noun:")
  userInput[8] = requestString("Enter a noun:")
  userInput[9] = requestString("Enter a noun:")
  userInput[10] = requestString("Enter a noun:")
  userInput[11] = requestString("Enter a noun:")
  
  printArticle(userInput)