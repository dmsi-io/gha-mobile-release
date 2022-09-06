import sys

if len(sys.argv) < 2:
    print("Must include a file to adjust")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    contents = f.readlines()
    f.close()


    def adjust_build_number(line):
        import re
        result = re.search(r"(.*)(\d+)(.*)", line, re.DOTALL)
        new_build_number = int(result.group(2)) + 1
        print("Setting buildNumber to %d" % new_build_number)
        return "%s%d%s" % (result.group(1), new_build_number, result.group(3))


    newContents = [
        adjust_build_number(x) if 'buildNumber' in x else x for x in contents
    ]
    with open(sys.argv[1], 'w') as wFile:
        wFile.writelines(newContents)
        wFile.close()