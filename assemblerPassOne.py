startingAddress=-1
tempAddress=-1
outputFile=open("outputPython.txt","w")
symbolTable=open("symbolTablePython.txt","w")
with open("input.txt","r") as inputfile :
	for line in inputfile:
		line=[word for word in line.split()]
		label=line[0]
		opcode=line[1]
		operand=line[2]
		if tempAddress!=-1:
			outputFile.write(tempAddress+"  "+label+"  "+opcode+"  "+operand+"\n")
			if label!="**":
				symbolTable.write(label+"  "+tempAddress+"\n");
			if opcode=="RESW":
				tempAddress+=3*stoi(operand);
			elif opcode=="BYTE":
				tempAddress+=1;
			elif opcode=="RESB" :
				tempAddress+=stoi(operand);
			else:
				tempAddress+=3;

		if tempAddress=="START":
			startingAddress=tempAddress;
			outputFile.write("      "+label+"  "+opcode+"  "+operand+"\n")
print("The length of program is = ",tempAddress-startingAddress-3); # I have subtracted 3 here because tempAddress add 3 
	# when it reads end opcode.

			




