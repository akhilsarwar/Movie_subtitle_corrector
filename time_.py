"""
    Time module - this module handles and manipulated time in various string formats
    For instance- 
        "123 <sep> 384 <sep> 3480 <sep> 830909" be a time in the format - "hour <sep> min <sep> sec <sep> millisec"
        <sep> can be any string value"

"""
class Time:

    #millissecond value of time 
    milliseconds = 0   

    #minute value of time
    minutes = 0

    #hour value of time
    hours = 0

    #second value of time
    seconds = 0


    #seperator seperating the second and millisecond value
    sep_sec_millisec = ':'

    #seperator seperating the minute and the second value 
    sep_min_sec = ':'

    #seperator seperating the hour and minute value 
    sep_hour_min = ':'






    #class constructor

    #by defualt all arguments are optional 

    #if no arguments are supplied then it instantiates a null time i.e "0:0:0:0", with a default seperator - ":"

    #code eg:
    """
        time = Time(hours = 1, minutes = 2, seconds = 3, millisecond = 4, sep = '>>')
        time.get_time()

        OUT:
            '1>>2>>3>>4'

    """

    def __init__(self, hours = 0, minutes = 0, seconds = 0, milliseconds = 0, sep = '', sep_sec_millisec = ':', sep_min_sec = ':', sep_hour_min = ':'):
        self.hours, self.minutes, self.seconds, self.milliseconds = hours, minutes, seconds, milliseconds

        if(len(sep) == 0):
            self.sep_sec_millisec = sep_sec_millisec
            self.sep_min_sec = sep_min_sec
            self.sep_hour_min = sep_hour_min
        else:
            self.sep_sec_millisec = sep
            self.sep_min_sec = sep
            self.sep_hour_min = sep







    #takes time in string format and converts it into a valid time format 

    #time_str is a positional argument and must be provided 

    #string format must be in "hour <sep> minute <sep> seconds <sep> milliseconds" where <sep> can be any string

    #if no seperators are provided then default seperator is ':'

    #if all seperators are same then only provide 'sep' arg

    #otherwise provide individual sep args (sep_sec_millisec, .......)

    #if both 'sep' arg and individual sep args are provided then 'sep' will be preferred  

    """
        time  = Time()
        time.str_time("23:659:45:3434", sep = ':')
        time.get_time()

        OUT:
           '33:59:48:434' 
    """

    def str_time(self, time_str, sep = '', sep_sec_millisec = ':', sep_min_sec = ':', sep_hour_min = ':'):
        if(len(sep) == 0):
            self.sep_sec_millisec = sep_sec_millisec
            self.sep_min_sec = sep_min_sec
            self.sep_hour_min = sep_hour_min
        else:
            self.sep_sec_millisec = sep
            self.sep_min_sec = sep
            self.sep_hour_min = sep

        self.hours, self.minutes, self.seconds, self.milliseconds = self._parse_time(time_str)
        self.add_time()







    #returns time in string format - hour <sep> minute <sep> second <sep> millisecond

    #if 'sep' arg is provided then, it overrides the default seperator args or the args provided at the time of instantiation

    """
        time  = Time()
        time.str_time("23:659:45:3434", sep = ':')
        time.get_time(sep = '>>')

        OUT:
           '33>>59>>48>>434' 
    """
    def get_time(self, sep = ''):
        time_str = ""
        if(len(sep) == 0):

            time_str = str(self.hours) + self.sep_hour_min + str(self.minutes) + self.sep_min_sec + str(self.seconds) + self.sep_sec_millisec + str(self.milliseconds)
        else:
            time_str = str(self.hours) + sep + str(self.minutes) + sep + str(self.seconds) + sep + str(self.milliseconds)
        return time_str



  
    #adds time 

    #if no args are provided time doesn't change  
    """
        time = Time()
        time.str_time("23:659:45:3434", sep = ':')
        time.add_time(hours = 1, minutes = 1, seconds = 2, milliseconds = 3)
        time.get_time(sep = '>>')

        OUT:
            '35>>0>>50>>437'

    """
    def add_time(self, hours = 0, minutes = 0, seconds = 0, milliseconds = 0):
        add_sec_buff = (self.milliseconds + milliseconds) // 1000
        self.milliseconds = (self.milliseconds + milliseconds) % 1000
        add_min_buff = (add_sec_buff + self.seconds + seconds) // 60
        self.seconds = (self.seconds + add_sec_buff + seconds) % 60
        add_hour_buff = (add_min_buff + self.minutes + minutes) // 60
        self.minutes = (self.minutes + minutes + add_min_buff) % 60
        self.hours = (self.hours + hours + add_hour_buff)

    def sub_time(self, hours = 0, minutes = 0, seconds = 0, milliseconds = 0):
        now = (1000 - self.milliseconds) + milliseconds
        milliseconds_now = (1000 - now) % 1000
        if milliseconds_now > 0:
            sec_red = (now) // 1000
        else:
            sec_red = (now) // 1000 - 1

        now = (60 - self.seconds) + seconds + sec_red
        seconds_now  = (60 - now) % 60
        if seconds_now > 0:
            min_red = (now) // 60
        else: 
            min_red = (now) // 60 - 1

        now = (60 - self.minutes) + min_red + minutes
        minutes_now = (60 - now) % 60
        if minutes_now > 0:
            hour_red = (now) // 60
        else:
            hour_red = (now) // 60 - 1

        try:
            assert(hour_red + hours <= self.hours)
            self.milliseconds = milliseconds_now
            self.seconds = seconds_now
            self.minutes = minutes_now
            self.hours -= (hours + hour_red)

        except:
            print('Invalid reduction time !!!')
            print('Time going out of bounds')
            print('Exiting.....')



    #parses the timedata given in string format

    def _parse_time(self, time_str):
        split_list = [self.sep_hour_min, self.sep_min_sec, self.sep_sec_millisec]
        time = []
        now = time_str
        for ind, split_string in enumerate (split_list):
            buffer_list = now.split(split_string, 1)
            time.append(int(buffer_list[0].strip(' ')))
            now = buffer_list[1]

        time.append(int(now.strip(' ')))
        return time



def main():

    t = Time()
    t.str_time("23*44--28>>00", sep_hour_min = '*', sep_min_sec = '--', sep_sec_millisec = '>>')
    print(t.get_time())
    t.sub_time(hours = 12, minutes = 58, seconds = 45, milliseconds = 0)
    print(t.get_time())


if __name__ == "__main__":
    main()
