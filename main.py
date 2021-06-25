from time_ import Time
import sys


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

            
def error(error_msg = "error !!!\n Exiting....."):
    print(error_msg)
    exit()

def main(argv):

    filename = argv[1]
    

    move = input('forward or backward? f or b\n').strip(' ')
    try:
        assert move == 'f' or move == 'b' or move == 'F' or move == 'B'
    except:
        error('Invalid Entry !!! \n Exiting ....')




    print('Enter the shift amount')
    try:
        shift_hours = int(input('hours : ').strip(' '))
        shift_minutes = int(input('minutes : ').strip(' '))
        shift_seconds = int(input('seconds : ').strip(' '))
        shift_milliseconds = int(input('milliseconds : ').strip(' '))

    except:
        error('Invalid Entry !!! \n Exiting ....')

    newfile = open("out", "w")
    with open(filename, "r+") as file:
        i = 0
        for line in file:
            if confirm(line):
                beg_time, end_time = extract_time(line)
                BEG = Time()
                BEG.str_time(beg_time, sep_hour_min = ':', sep_min_sec = ':', sep_sec_millisec = ',')
                END = Time()
                END.str_time(end_time, sep_hour_min = ':', sep_min_sec = ':', sep_sec_millisec = ',')
                if move == 'f' or move == 'F':
                    BEG.add_time(hours = shift_hours, minutes = shift_minutes, seconds = shift_seconds, milliseconds = shift_milliseconds)
                    END.add_time(hours = shift_hours, minutes = shift_minutes, seconds = shift_seconds, milliseconds = shift_milliseconds)
                else:

                    BEG.sub_time(hours = shift_hours, minutes = shift_minutes, seconds = shift_seconds, milliseconds = shift_milliseconds)
                    END.sub_time(hours = shift_hours, minutes = shift_minutes, seconds = shift_seconds, milliseconds = shift_milliseconds)

                newline = process_newline(BEG, END)
                newfile.write(newline)
            else:
                newfile.write(line)

    print('change successful')


if __name__ == "__main__":
    main(sys.argv)
