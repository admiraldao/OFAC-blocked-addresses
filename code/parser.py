"""
Helper script for OFAC updates.

Opens a file, reads all of the words that look like ETH addresses
(Word breaking done on whitespace or punctuation)
Reads addresses.txt
Collates, outputs
"""
import argparse
import re
from eth_utils import to_checksum_address

addresses = set()

parser = argparse.ArgumentParser(description='Read and collate ETH addresses.')
parser.add_argument('filename', type=str, help="Filename to read")

args = parser.parse_args()
fname = args.filename

with open(fname) as inputfile:
	for line in inputfile:
		for word in re.findall(r"\w+|[^\w\s]", line):
			try:
				addy = to_checksum_address(word)
			except:
				continue
			addresses.add(addy)

with open("../addresses.txt") as inputfile:
	for line in inputfile:
		for word in line.split():
			try:
				addy = to_checksum_address(word)
			except:
				continue
			addresses.add(addy)

the_list = sorted(list(addresses), key=lambda x: x.lower())
for addy in the_list:
	print(addy)