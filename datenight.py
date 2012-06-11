#!/usr/bin/python

from datetime import date

kara_and_jake_available = set([])
kjellrun_and_luke_available = set([])
sam_and_sam_available = set([date(year=2012, month=6, day=15),
                             date(year=2012, month=6, day=16)])

kj_babysitter = set([])
kl_babysitter = set([])
ss_babysitter = set([])

def print_dates(dates):
    for d in dates:
        print d.strftime("%m/%d/%Y")

def main():
    global kara_and_jake_available, kjellrun_and_luke_available, sam_and_sam_available
    global kj_babysitter, kl_babysitter, ss_babysitter

    possible_dates = reduce(lambda x,y: x.intersection(y),
                            [sam_and_sam_available,
                             kara_and_jake_available,
                             kjellrun_and_luke_available])

    if possible_dates == None or len(possible_dates) == 0:
        print "Could not find any dates for the babysitters"
        return

    print "Here are some dates to ask the babysitters:"
    print_dates(possible_dates)
    print
    
    possible_dates = map(lambda x: x.intersection(possible_dates), [kj_babysitter,
                                                                    kl_babysitter,
                                                                    ss_babysitter])

    possible_dates = reduce(lambda x,y: x.intersection(y), possible_dates)

    if possible_dates == None or len(possible_dates) == 0:
        return

    print "DATE NIGHT!!!:"
    print_dates(possible_dates)

if __name__ == "__main__":
    main()
