from collections import defaultdict

def give1():
    data = defaultdict(list)
    noteam=int(input("enter the number of teams"))
    no_team=noteam
    interval=1
    while(True):
        if(no_team<200):
            interval=200/no_team
            break
        else:
            no_team=no_team-200
    i=1
    while(noteam>0):
        if(noteam>=200):
            teamid=input("enter team id")
            data[i].append(teamid)
            i=i+1
            noteam=noteam-1
        if(i>200):
            i=1
        if(noteam<200):
            teamid=input("enter team id")
            data[i].append(teamid)
            i=i+interval
            noteam=noteam-1
    print(data)

def give2():
    no=200
    for ii in range(3,8):
        data = defaultdict(list)
        number_of_bucket=int(input("enter number of buckets in this round"))    
        k=no

        reminder=no%number_of_bucket
        interval=int(number_of_bucket/reminder)
        
        i=1
        
        while(k>0):
            if(k>number_of_bucket):
                data[i].append(k)
                i=i+1
                k=k-1
                
                
            if(i==number_of_bucket):
                i=1
            if(k<=number_of_bucket):
                data[i].append(k)
                
                i=i+interval
                k=k-1

        print(data)
        no=number_of_bucket

            

#give1()
give2()