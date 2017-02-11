from time import gmtime, strftime
import th1w
import sendrf 
import thuser
import thstatus 
MSG=['PF','PO']
DELTA_UP=0.2
DELTA_DOWN=0.3
current=th1w.read_temp() 
desire=thuser.getUser()
STATUS=thstatus.getStatus()
if (float(STATUS) == 1):  # Currently On 
    if (current>desire+DELTA_UP):
        # GO TO OFF 
        STATUS=0

else:
    if (current<desire-DELTA_DOWN):
        # GO TO ON
        STATUS=1

# final status 
print strftime("%Y-%m-%d %H:%M:%S", gmtime()),current,desire,STATUS,MSG[int(STATUS)]
sendrf.rfSend(MSG[int(STATUS)]) 
thstatus.setStatus(str(STATUS)) 
