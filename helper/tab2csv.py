# Python program to convert .tsv file to .csv file
# importing re library
import re

# reading given tsv file
with open("noncodingModel.tab", 'r') as myfile:
    with open("noncodingModel.csv", 'w') as csv_file:
        for line in myfile:

            # Replace every tab with comma
            fileContent = re.sub("\t", ",", line)

            # Writing into csv file
            csv_file.write(fileContent)

# output
print("Successfully made csv file")
