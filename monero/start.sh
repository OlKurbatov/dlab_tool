#!/bin/bash
rm -r /home/$USER/.monero/node*
local_nodes_ports=(28080 38080 48080 58080)
geometry=(90x20+0+0 90x20+950+0 90x20+0+500 90x20+950+500)
command="xfce4-terminal"

printf "Enter type of setup:\n1)Multiple nodes on the local machine\n"
read setup

if [ $setup == "1" ]
then
	for ((i=0; i< ${#local_nodes_ports}-1; ++i));
	do
		node_port=${local_nodes_ports[$i]}
		p2port=$node_port
		rpc_port=${local_nodes_ports[$i]::${#local_nodes_ports[$i]}-1}1
		zmq_rpc_port=${local_nodes_ports[$i]::${#local_nodes_ports[$i]}-1}2

		nodes_ports_to_add=(${local_nodes_ports[@]/$node_port})
                node_command="./monerod --testnet --no-igd --data-dir node$i --p2p-bind-ip 127.0.0.1 --log-level 0 --fixed-difficulty 100"
		
		node_command="$node_command --p2p-bind-port $p2port --rpc-bind-port $rpc_port --zmq-rpc-bind-port $zmq_rpc_port"

		for ((j=0; j< ${#nodes_ports_to_add}-2; ++j));
		do
			add_node="--add-exclusive-node 127.0.0.1:${nodes_ports_to_add[$j]}" 
			node_command="$node_command $add_node"
		done

		wallet_create_command="./monero-wallet-cli --testnet --generate-new-wallet node$i/moneybag.bin  --password 'bit' "
		#wallet_enter="./monero-wallet-cli --testnet --trusted-daemon --wallet-file node$i/moneybag$i.bin --password '' --log-file node$i/moneybag$i.log"


		node_open_command="$command -T node$i-console --working-directory /home/$USER/.monero/ -e '$node_command' -H 
--tab -T wallet$i-console --working-directory /home/$USER/.monero/ -e '$wallet_create_command' -H --geometry=${geometry[$i]}"
		eval $node_open_command
	done
fi
