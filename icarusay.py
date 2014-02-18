#!/usr/bin/python
#
#  icarusay.py
#  
#  Written by Earl Cash <erl@codeward.org> in 2014.


import sys, os, getopt, math, time, signal

def sig_handler (signo, frame):
	sys.exit (signo)

def usage ():
	print "Usage:"
	print " "+ os.path.basename (sys.argv[0]) +" [OPTIONS]"
	print "\nOptions:"
	print " -l=N\tprint N lines of a message (if N is not an even number, addition will occur)"	
	print " -n=N\tprint a message N times (if N is equal to 0, infinity is assumed)"
	print " -m=N\tchoose a message being printed (valid range 0-1)"
	print " -s=N\tspeed of typing an individual line in seconds (supports numbers with decimal precision)"
	print " -h\tdisplay this usage text"

def main (argv):

	messages = {
		0: [ "ICARUS IS LOOKING FOR YOU" ],
		1: [ "ICARUS FOUND YOU!!!", "RUN WHILE YOU CAN!!!" ]
	}

	opts_data = {
		"p": os.path.basename (sys.argv[0]),
		"lines": 20,
		"repeat": 1,
		"message_type": 0,
		"speed": 0
	}

	try:
		opts, args = getopt.gnu_getopt (argv[1:], "l:n:m:s:h")
	except getopt.GetoptError as err:
		usage ()
		sys.exit (1)

	for opt, arg in opts:
		if opt == "-l":

			try:
				opts_data["lines"] = int (arg)
			except ValueError:
				print (opts_data["p"]+": invalid number (param -l)")
				sys.exit (1)

			if (opts_data["lines"] % 2) != 0:
				opts_data["lines"] += 1

		elif opt == "-n":

			try:
				opts_data["repeat"] = int (arg)
			except ValueError:
				print (opts_data["p"]+": invalid number (param -n)")
				sys.exit (1)

		elif opt == "-m":

			try:
				opts_data["message_type"] = int (arg)
			except ValueError:
				print (opts_data["p"]+": invalid number (param -m)")
				sys.exit (1)

			if not opts_data["message_type"] in messages:
				print (opts_data["p"]+": undefined message index")
				sys.exit (1)

		elif opt == "-s":

			try:
				opts_data["speed"] = float (arg)
			except ValueError:
				print (opts_data["p"]+": invalid number (param -s)")
				sys.exit (1)
				
		elif opt == "-h":
			usage ()
			sys.exit (0)

	if opts_data["message_type"] == 0:
		repeat_counter = 0
		while True:
			for line in range (opts_data["lines"]):
				print ((" " * line)+messages[0][0])
				time.sleep (opts_data["speed"])

			repeat_counter += 1

			if opts_data["repeat"] > 0 and repeat_counter >= opts_data["repeat"]:
				break

	elif opts_data["message_type"] == 1:
		repeat_counter = 0
		while True:
			for line in range (int (math.floor (float (opts_data["lines"]) / 2.0))):
				print ((" " * line)+messages[1][0])
				time.sleep (opts_data["speed"])

			for line in range (int (math.floor (float (opts_data["lines"]) / 2.0)) - 1, -1, -1):
				print ((" " * line)+messages[1][1])
				time.sleep (opts_data["speed"])

			repeat_counter += 1

			if opts_data["repeat"] > 0 and repeat_counter >= opts_data["repeat"]:
				break	

if __name__ == "__main__":
	signal.signal (signal.SIGINT, sig_handler)
	signal.signal (signal.SIGTERM, sig_handler)
	main (sys.argv);

