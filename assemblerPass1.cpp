#include<bits/stdc++.h>
#include<string>
using namespace std;
int main()
{
	int startingAddress=-1,tempAddress=-1;
	string label,opcode,operand;
	ifstream file("input.txt");
	ofstream outputFile("output.txt");
	ofstream symbolTable("symbolTable.txt");
	while(file>>label>>opcode>>operand){
		// cout<<"label="<<label<<"\n";
		// cout<<"opcode="<<opcode<<"\n";
		// cout<<"operand="<<operand<<"\n";
		if(tempAddress!=-1){
			outputFile<<tempAddress<<"  "<<label<<"  "<<opcode<<"  "<<operand<<"\n";
			cout<<tempAddress<<"  "<<label<<"  "<<opcode<<"  "<<operand<<"\n";

			if(label!="**"){
				symbolTable<<label<<"  "<<tempAddress<<"\n";
			}
			if(opcode=="RESW"){
				tempAddress+=3*stoi(operand);
			}else if(opcode=="BYTE"){
				tempAddress+=1;
			}else if(opcode=="RESB"){
				tempAddress+=stoi(operand);
			}else{
				tempAddress+=3;
			}
		}
		if(opcode=="START"){
			tempAddress=stoi(operand);
			startingAddress=tempAddress;
			// cout<<startingAddress;
			outputFile<<"      "<<label<<"  "<<opcode<<"  "<<operand<<"\n";
			cout<<"      "<<label<<"  "<<opcode<<"  "<<operand<<"\n";
		}

	}
	cout<<"The length of program is = "<<tempAddress-startingAddress-3<<"\n"; //I have subtracted 3 here because tempAddress add 3 
	// when it reads end opcode.
}
//g++ -std=c++11 assemblerPass1.cpp