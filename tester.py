import os
import sys

if not os.path.isfile("the3.c"):
	sys.exit()

os.system("gcc -Wall -ansi -pedantic-errors the3.c -o the3 -lm")

total_cases = 1881
passed_cases = 0

for i in range(1, 1882):
	with open(f"test/outputs/output{i}.txt", "r") as expected:
		expected_output = expected.read()

	os.system(f"./the3 < test/cases/case{i}.txt > given_output.txt")

	with open("given_output.txt", "r") as given:
		given_output = given.read()

	if given_output == expected_output:
		passed_cases+=1
		print(f"PASSED test case {i}.")
	else:
		print(f"FAILED test case {i}.\n\nExpected Output:\n" + expected_output + "\nGiven Output:\n" + given_output)

os.remove("given_output.txt")

print("\nYour Grade:", (passed_cases/total_cases) * 100)