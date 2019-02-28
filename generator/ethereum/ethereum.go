package main

import (
	"context"
	"crypto/ecdsa"
	"fmt"
	"github.com/ethereum/go-ethereum/accounts"
	"github.com/ethereum/go-ethereum/accounts/keystore"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/crypto"
	"github.com/ethereum/go-ethereum/ethclient"
	"io/ioutil"
)



var nodes_path string = "/home/meksvinz/Projects/dlab_tool/ethereum/"

type Account struct {
	address common.Address
	nonce uint64
}

type Node struct {
	name string
	connect ethclient.Client
	account Account
	privK ecdsa.PrivateKey
	keystore_path string

}

var nodes = make([]Node, 0, 10)

func (node *Node)NewAccount()  {
	ks := keystore.NewKeyStore(node.keystore_path, keystore.StandardScryptN, keystore.StandardScryptP)
	fmt.Println(node.keystore_path)

	pk, _ := crypto.GenerateKey()
	account, err := ks.ImportECDSA(pk, "12345")

	if err == nil{
		node.account.address = account.Address
		node.account.nonce = 0
		node.privK = *pk
		fmt.Println(node.account.address.Hex())
	}

}

func main()  {
	listdir, _ := ioutil.ReadDir(nodes_path)
	for _, sub := range listdir{
		name := sub.Name()
		if name[:len(name)-1] == "node"{
			connect, err := ethclient.Dial(nodes_path+"/"+name+"/geth.ipc")
			if err == nil{
				fmt.Printf("Connect to %s success\n", name)
				node := Node{connect: *connect, name:name, keystore_path:nodes_path+"/"+name+"/keystore"}
				nodes = append(nodes, node)
				}
			}
	}
	//nodes[0].NewAccount()
	//fmt.Println(nodes[0].account.Address.Hex())
	for _, node := range nodes{
		fmt.Printf("Generating new account for %s\n", node.name)
		node.NewAccount()
		nonce, _ := node.connect.PendingNonceAt(context.Background(), node.account.Address)
		fmt.Println(nonce)
		}
	for {
		for _, node := range nodes{
			for _, resipient := range nodes{
				tx := types.NewTransaction(node.account.nonce, resipient.account.address, )
			}
		}
	}

	}