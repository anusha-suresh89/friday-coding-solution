import re
from addresses import *


pattern = '(^(No|NO|no|#)*(\\s)*([0-9])+(\\s)*([a-z]|[A-Z])*)|((No|no|NO|#)*(\\s)*[0-9]+(\\s)*([a-z]|[A-Z])*$)'


def get_house_number(address, re_pattern):
	matches = re_pattern.search(address)
	if matches:
		return matches.group(0).strip()
	else:
		return ''

def get_street(address,house_number):
	street = address.replace(house_number, '')
	return street.strip()

def main():
	re_pattern = re.compile(pattern)
	parsed_addresses = []
	for entry in addresses:
		house_number = get_house_number(entry, re_pattern)
		street = get_street(entry, house_number)
		parsed_addresses.append({'address': entry, 'house_number': house_number, 'street': street})
	return parsed_addresses

if __name__ == '__main__':
	main()



