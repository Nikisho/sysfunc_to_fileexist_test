def sysfunc_exist_to_filexists(files: list) -> None:
    for file in files:
        string: str = "sysfunc(exist("
        new_string: str = "fileexists(datasetname="

        with open(file, "r") as infile:
            filedata: str = infile.read()
            infile.seek(0)
            lines: list = infile.readlines()
        infile.close()
            
        for line in lines:
            if string in line:

                target_line: str = line.replace(string, new_string)

                flag: int = 0

                target_line_length: int = len(target_line)

                for i in range(target_line_length):
                    char: str = target_line[i]
                    if target_line[i:i+7] == 'exists(':
                        flag += 1
                    if flag == 1 and char == ')':
                        target_line = target_line.replace(char,'',1)
                        flag -= 1
                        break
                print(target_line)
                filedata: str = filedata.replace(line, target_line)   
                print(filedata)             

        with open(file, 'w') as outfile:
            # outfile.write(infile)                    
            outfile.write(filedata)
        outfile.close()
    
sysfunc_exist_to_filexists(['test1.sas','test2.sas'])


