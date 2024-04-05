#!/bin/bash
core_dir="$1"

while true; do
    printf "> "
    read command

    if [ "$command" == "exit" ]; then
        exit
    else
        exec="$core_dir/ipfs/ipfs $command"
        eval $exec
    fi
done

