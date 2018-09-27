#TODO: complete header
#This module generates README.md
import getopt, sys
import os

class ReadME:

    def __init__(self,prj_name,language):

        self.prj_name = prj_name
        self.language = language
        self.readme_txt = ""
        self.readme_txt += "# %s\n"%(self.prj_name)
        self.readme_txt += "A simple %s project...\n\n"%(self.language)
        self.readme_txt += "### Source code\n"
        self.readme_txt += "https://github.com/...\n\n"
        self.readme_txt += "### Project Dependencies\n"
        self.readme_txt += "* Foo1\n"
        self.readme_txt += "* Foo2\n\n"
        self.readme_txt += "### Foo Title\n"
        self.readme_txt += "Foo description\n"
        self.readme_txt += "```\n"
        self.readme_txt += "Foo command\n"
        self.readme_txt += "```\n"
        self.path_res = "./test_readme_md_out/"

    def print(self):
        print(self.readme_txt)

    def save(self):
        try:  
            os.mkdir(self.path_res)
        except OSError:  
            print ("Creation of the directory %s failed" % self.path_res)
        else:  
            print ("Successfully created the directory %s " % self.path_res)
        f = open(self.path_res + "README.md","w")
        f.write(self.readme_txt)
        f.close()
            

def usage():
    stdout = ""
    stdout += "Usage examples:\n"
    stdout += "python readme.py -l cpp -p boost_sharedmem\n"
    print(stdout)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "sl:p:ho:v", ["save","language=","project_name=","help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print (str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    
    rdme = None
    output = None
    verbose = False
    project_name = None
    language = None
    save_flag = False
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
        elif o in ("-s", "--save"):
            save_flag = True
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

    if(rdme != None and save_flag):
        rdme.save()

if __name__ == "__main__":
    main()