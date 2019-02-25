package main

import (
	"context"
	"fmt"
	"github.com/ethereum/go-ethereum/crypto"
	"github.com/ethereum/go-ethereum/ethclient"
	"io/ioutil"
)



var nodes_path string = "/home/meksvinz/Projects/dlab_tool/ethereum/"

type Node struct {
	name string
	connect ethclient.Client
}

var nodes = make([]Node, 0, 10)

func wallet_stuff (){
	privateKey, err := crypto.GenerateKey()
}

func main()  {
	listdir, _ := ioutil.ReadDir(nodes_path)
	for _, sub := range listdir{
		name := sub.Name()
		if name[:len(name)-1] == "node"{
			fmt.Println(nodes_path+"/"+name+"/geth.ipc")
			connect, err := ethclient.Dial(nodes_path+"/"+name+"/geth.ipc")
			if err == nil{
				fmt.Printf("Connect to %s success\n", name)
				node := Node{connect: *connect, name:name}
				nodes = append(nodes, node)
				}
			}
	}
	for _, node := range nodes{
		result, _ := node.connect.NetworkID(context.Background())
		fmt.Println(node.name, result)
	}
}