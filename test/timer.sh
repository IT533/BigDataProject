#!/bin/sh
echo "execution: $1\nscript: $2\ninput: $3\noutput: $4" > $"timer/timer"
echo "--------------------------------------------------------------------------------" >> $"timer/timer"
date >> $"timer/timer"
echo "--------------------------------------------------------------------------------" >> $"timer/timer"


eval $"$1 $2 $3 > $4"


date >> $"timer/timer"
echo "--------------------------------------------------------------------------------" >> $"timer/timer"
