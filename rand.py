import random, sys, argparse, timeit


UTF_MAX = int("0xc3bf", 0)
ASCII_MAX = int("0x7e", 0)
ASCIIEX_MAX = int("0xff", 0)


class usage():
	soft_descript = "Generates randomized string using extended ascii and UTF-8 chars and stores it in a file"

	a_descript = "Generate a ranomdized string only from the standard ASCII table"
	e_descript = "Uses the extended ASCII table as well"
	v_descript = "Shows the progress"

	len_descript = "Amount of chars that will be generated"
	file_descript = "Filename to save the string to"



class gen():
	def string(args):
		s = []
		i = 0
		lens = args.int
		filename = args.string
		

		
		if args.ascii == True:
			for i in range(lens):
				asc = random.randrange(32, ASCII_MAX)
				s.append(chr(asc))
				#if args.verbose == True:
				#	print(round((i / lens) * 100))
				

		elif args.extend == True:
			for i in range(lens):
				ascex = random.randrange(32, ASCIIEX_MAX)
				s.append(chr(ascex))
				#if args.verbose == True:
				#	print(i / lens)
				
		else:
			for i in range(lens):
				ru = random.randrange(UTF_MAX)
				asc = random.randrange(32, ASCIIEX_MAX)
				s.append(chr(ru)) or s.append(chr(asc))
				#if args.verbose == True:
				#	print(i / lens)
				


		key = "".join(s)
		f = open(filename, "w", encoding="utf-8")
		f.write(key)
		f.close()
		
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def main():
	parser = argparse.ArgumentParser(description=usage.soft_descript)
	parser.add_argument("-a", "--ascii", help=usage.a_descript, action="store_true")
	parser.add_argument("-e", "--extend", help=usage.e_descript, action="store_true")
	parser.add_argument("-v", "--verbose", help=usage.v_descript, action="store_true")
	parser.add_argument("int", metavar="length", type=int, help=usage.len_descript)
	parser.add_argument("string", metavar="filename", type=str, help=usage.file_descript)
	args = parser.parse_args()
	
	if(args.ascii == True and args.extend == True):
		print("Error: Only one option is allowed")
		sys.exit()
	wrapped = wrapper(gen.string, args)
	print(timeit.timeit(wrapped, number=1))
	


if __name__ == "__main__":
	main()


