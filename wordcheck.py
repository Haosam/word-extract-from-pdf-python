import re
from collections import Counter
import csv
from itertools import islice
import os

#filename="./text/30_asean_summit.pdf.txt"
filedir = "./text/"
numLines = 0
numWords = 0
numChars = 0
"""
ASEAN = 0
I = 0
soverign = 0
territory = 0
"""

for txt in os.listdir(filedir):

	fileExtension = txt.split(".")[-1]
	if fileExtension == "txt":
		filename = filedir + txt
		file = open(filename, encoding="utf8")
		message = file.read()
		print(message)
		words = re.findall(r"[^\W_]+", message, re.MULTILINE)
		print(len(words))
		#print(words)

		count_words = Counter(words)
		print(count_words)

		print(len(count_words))

		full_list = [{k: v} for k, v in count_words.items()]
		print(full_list)
		print(len(full_list))

		csv_filename = "./" + txt + ".csv"

		with open(csv_filename, mode='w') as csv_file:
			writer = csv.writer(csv_file)

			for key, value in count_words.items():
				writer.writerow([key, value])




