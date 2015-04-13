This is a tool that explores how well kill signals are caught via atexit vs signal.

test-signal.sh and test-atexit.sh will each launch the corresponding python script,
send a kill signal, then try to kill the pid file after.

For some reason atexit isn't working at all


This means the process was killed and the cleanup function called
  Python sleeping
  Killing with INT
  CLEANED!
  ./test-command.sh: line 26: kill: (5465) - No such process

This means the process was not killed, and cleanup function not called
  Python sleeping
  Killing with QUIT
