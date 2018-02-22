"""

dns.py

Author: Tina Aquino

"""


import argparse
import socket


def getIPAddr(args):
	for i in range (len(args.domain)):
		try:
			IPAddr = socket.gethostbyname(args.domain[i])
			print(args.domain[i] + ": " + IPAddr)
		except:
			print("Error: Unknown domain.")

def getHostName(args):
	for i in range(len(args.addr)):
		try:
			host_name = socket.gethostbyaddr(args.addr[i])
			host_name = host_name[0]
			print(args.addr[i] + ": " + host_name)
		except:
			print("Error: Unknown IP address.")


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Get IP addresses.')
	parser.add_argument('-d', '--domain', default = False, nargs = '+', help = 'Retrieves IP address of the domain')
	parser.add_argument('-a', '--addr', default = False, nargs = '+', help = "Retrieves host name of the IP address")
	args = parser.parse_args()


	try:
		if args.domain is not False:
			getIPAddr(args)
		elif args.addr is not False:
			getHostName(args)
		else:
			parser.print_help()
	except:
		print("Please enter valid arguments.")
