import webbrowser
import time
break_count = 0
total_breaks = 3
print "the current time is: " , time.ctime
while break_count < total_breaks:
   print 'This is a time for your break.'
   time.sleep(5)
   webbrowser.open(r"https://www.youtube.com/watch?v=0xENUOoAPsk")
   break_count +=1