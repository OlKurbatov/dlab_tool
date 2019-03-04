#!/bin/bash
core_dir="$1"

while true; do
printf "> "
read command
exec="$core_dir/ipfs/ipfs $command"
eval $exec
done