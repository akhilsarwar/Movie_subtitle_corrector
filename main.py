from time_ import Time


def confirm(line):
    colon_cnt  = 0
    for char in line:
        if char == ':':
            colon_cnt  += 1
    flag = False
    bypasser = "-->" 
    if bypasser in line and colon_cnt  == 4:
        return True
    else:
        return False

def extract_time(line):
    beg_time = ""
    end_time = ""
    end_time_start_at = 0
    for ind, char in enumerate(line):
        if char == '-':
            assert line[ind + 1] == '-' and line[ind + 2] == '>'
            end_time_start_at = ind + 3
            break
        else:
            beg_time += char

    end_time = line[end_time_start_at:]
    beg_time = beg_time.strip(' ')
    end_time = end_time.strip(' ')
    return beg_time, end_time


def process_newline(BEG, END):
    newline = ""
    newline = str(BEG.get_time()) + ' ' + '-->' + ' ' + str(END.get_time()) + '\n'
    return newline

            


def main():

    newfile = open("/home/akku/Downloads/After We Collided (2020) [720p] [BluRay] [YTS.MX]/newsrt.srt", "w")
    with open("subs", "r+") as file:
        i = 0
        for line in file:
            if confirm(line):
                beg_time, end_time = extract_time(line)
                BEG = Time()
                BEG.str_time(beg_time, sep_hour_min = ':', sep_min_sec = ':', sep_sec_millisec = ',')
                END = Time()
                END.str_time(end_time, sep_hour_min = ':', sep_min_sec = ':', sep_sec_millisec = ',')
                BEG.add_time(seconds = 38, milliseconds = 500)
                END.add_time(seconds = 38, milliseconds = 500)
                newline = process_newline(BEG, END)
                newfile.write(newline)
            else:
                newfile.write(line)


if __name__ == "__main__":
    main()
