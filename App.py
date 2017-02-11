from time import gmtime, strftime
import th1w
import sendrf 
import thuser
import thstatus 
MSG=['PF','PO']
DELTA_UP=0.0 # Stops the boiler as soon as the temperature reaches the ref
DELTA_DOWN=0.3 # starts the boiler at Tref-0.3°C

current=th1w.read_temp() 
desire=thuser.getUser()
STATUS=thstatus.getStatus()
# Programmed as a finite state automata 
if (float(STATUS) == 1):  # Currently On 
    if (current>desire+DELTA_UP):
        # GO TO OFF 
        STATUS=0

else:
    if (current<desire-DELTA_DOWN):
        # GO TO ON
        STATUS=1

# Output (stored in log.txt when started by CRON)
print strftime("%Y-%m-%d %H:%M:%S", gmtime()),current,desire,STATUS,MSG[int(STATUS)]

# Sends to the boiler 
sendrf.rfSend(MSG[int(STATUS)]) 
thstatus.setStatus(str(STATUS)) 
