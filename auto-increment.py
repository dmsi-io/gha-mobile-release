import sys

if len(sys.argv) < 2:
    print("Must include a file to adjust")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    contents = f.readlines()
    f.close()


    def increment_build_number(line):
        import re
        result = re.search(r"(.*)(\d+)(.*)", line, re.DOTALL)
        new_build_number = int(result.group(2)) + 1
        print("Setting buildNumber to %d" % new_build_number)
        return "%s%d%s" % (result.group(1), new_build_number, result.group(3))


    newContents = [
        # Increment build number if 'buildNumber' is in the text of the line
        (increment_build_number(line) if 'buildNumber' in line else line) for line in contents
    ]
    with open(sys.argv[1], 'w') as wFile:
        wFile.writelines(newContents)
        wFile.close()
