#!/bin/bash

echo "roll.sh v1"

while true
do

read -p "> " arg

# exit
if [ $arg = "exit" ] || [ $arg = "e" ]; then
	exit

# help
elif [ $arg = "help" ] || [ $arg = "h" ]; then
	echo -e "<number>\ncoin/c\nexit/e"

# coin
elif [ $arg = "coin" ] || [ $arg = "c" ]; then
	if [ $((1 + $RANDOM % 2)) = 1 ]; then
		echo "heads"
	else
		echo "tails"
	fi

# dice
elif [ "$arg" -eq "$arg" ] 2>/dev/null; then
	echo $((1 + $RANDOM % $arg))
else
	echo "Argument not found, type help for a list."
fi

done