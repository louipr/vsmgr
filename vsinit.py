#TODO: complete header
#This module initializes the whole workspace  
import getopt, sys
from readme import ReadME


def usage():
    stdout = ""
    stdout += "Usage examples:\n"
    stdout += "python vsinit.py -l cpp -p boost_sharedmem\n"
    print(stdout)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "l:p:ho:v", ["language=","project_name=","help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print (str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    project_name = None
    language = None
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        elif o in ("-p", "--project_name"):
            project_name = a
        elif o in ("-l", "--language"):
            language = a
        else:
            assert False, "unhandled option"
    # ...

    if(not(not(project_name)) 
    and not(not(language))):
        rdme = ReadME(project_name,language)
        rdme.print()
    else:
        print("Invalid command entry")
        usage()
        assert False, "unhandled option"


if __name__ == "__main__":
    main()