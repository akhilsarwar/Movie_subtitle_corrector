class Time:
    milliseconds = 0
    minutes = 0
    hours = 0
    seconds = 0

    def __init__(self, h, m, s, milli, time_str):
        self.hours, self.minutes, self.seconds, self.milliseconds = self.parse_time(time_str)

    def get_time(self, h, m, s, milli):
        time_str = ""
        time_str = str(h) + ':' + str(m) + ':' + str(s) + ',' + str(milli)
        return time_str
    
    def add_time(self, h, m, s, milli):
        self.hours += h
        self.minutes += m
        slef.seconds += s
        self.milliseconds += milli
    
    def parse_time(self, time_str):
        parsed_list = time_str.split(':')
        hours = parsed_list[0]
        minutes = prased_list[1]
        parse_seconds = parsed_list[2].split(',')
        seconds = parse_seconds[0]
        milliseconds = parse_seconds[1]
        return hours, minutes, seconds, milliseconds
        
        

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

            


def main():
    with open("subs", "r+") as file:
        i = 0
        for line in file:
            #if i < 100:
            #    print(line)
            #    i+=1
            #else:
            #    break;
            if confirm(line):
                beg_time, end_time = extract_time(line)
                print(beg_time, end_time)
                BEG_, END_ = Time(beg_time), Time(end_time)
                BEG_.add(0, 0, )

if __name__ == "__main__":
    main()
