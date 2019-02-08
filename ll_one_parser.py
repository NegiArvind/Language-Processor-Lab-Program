from first_follow_function_predictive_parser import *
parse_table={}

def is_this_a_non_terminal(ch):
	if ord(ch)>=65 and ord(ch)<91:
		return True
	else:
		return False

def put_it_into_table(var,production):
	# print("var ",var,"production",production)
	if is_this_a_non_terminal(production[0]):
		# print("hiiiiiiiiiii")
		for first_of_alpha in first[production[0]]:
			# print("Going inside")

			if(parse_table.get(var)==None):
				parse_table[var]={}
			parse_table[var][first_of_alpha]=str(var+"->"+production)
	elif production[0]=='e': # if the production is like A->epsilon then this if condition will be true
		for follow_of_var in follow[var]:
			if(parse_table.get(var)==None):
				parse_table[var]={}
			parse_table[var][follow_of_var]=str(var+"->"+production)
	else:
		if(parse_table.get(var)==None):
				parse_table[var]={}
		parse_table[var][production[0]]=str(var+"->"+production)

def build_parse_table():
	for ch in order:
		for j in range(len(variable[ch])):
			# print("hello")
			put_it_into_table(ch,variable[ch][j])

def parse_the_input_string(input_string):
	tempStack=[]
	input_string+='$'
	tempStack.append('$')
	tempStack.append(order[0])
	i=0
	while i<len(input_string):
		print(tempStack,'\t',input_string[i:len(input_string)])
		stack_top=tempStack.pop()
		if is_this_a_non_terminal(stack_top):
			try:
				valid_production=parse_table[stack_top][input_string[i]]
				for j in range(len(valid_production)-1,2,-1): # Production is in the form A->{something} so 
				  # i will push variable into stack from right hand side till '>' symbol
					if valid_production[j]!='e': # if the production is like A->epsilon then i will not do 
					# anything becuase element is already popped out
						tempStack.append(valid_production[j])
						# print("valid production",valid_production[j])
					
				# print(tempStack)
				# print("harami")
			except :
				print("Given Input String can not be parsed")
				break;
		elif input_string[i]==stack_top: # if input_symbol is equal to top of the stack
			if input_string[i]=='$':
				print("Given Input String is sucessfully parsed")
				break; 
			else:
				# print("input_symbol matched")
				i+=1 #increment input_pointer



print("Order",order)
build_parse_table()
print("Parse Table :",parse_table)

inputString=input("Enter the string which you want to parse\n")
parse_the_input_string(inputString)



