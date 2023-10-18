import time

runebook_serial = 0x41C6A32A
runebook_gumpid = 1431013363
runebook_actionid = 11
max_timeout = 3
error = False

ppos_start = Player.Position
ppos = ppos_start


Items.UseItem(runebook_serial)
Gumps.WaitForGump(runebook_gumpid, 1000)


time_end = time.time() + max_timeout
Gumps.SendAction(runebook_gumpid, runebook_actionid )

while True:
    if ppos.X != ppos_start.X: 
        Player.HeadMessage(138,"Y changed")
        break
    if ppos.Y != ppos_start.Y: 
        Player.HeadMessage(178,"X changed")
        break
    if time.time() > time_end: 
        error = True
        Player.HeadMessage(138,"Timeout")
        break
    
    dt = float(time_end - time.time())
    ppos = Player.Position
    Misc.Pause(200)
    Player.HeadMessage(200,"Still waiting ({:.1f}s)".format(dt))
#    
if error:
    Player.HeadMessage(138,"Error, please try again.")
else:
    Player.HeadMessage(178,"Arrived")