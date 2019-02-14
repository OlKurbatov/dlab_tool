#!/bin/bash

IPADDRESS="$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' keosd)"

echo "Complete output: ${IPADDRESS}"
# set alias

shopt -s expand_aliases
#alias cleos='docker exec -it nodeos /opt/eosio/bin/cleos --url http://localhost:8888 --wallet-url http://${IPADDRESS%/*}:9876'

