import bitcoin.rpc
import bitcoin
from bitcoin.core import b2lx
import sys, os, time, termios, tty, hashlib

bitcoin.SelectParams("regtest")
nodes = []
class Node():
    def __init__(self, rpc_user, rpc_password, rpc_port):
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password
        self.rpc_port = rpc_port
        self.connect = bitcoin.rpc.Proxy(service_url="http://{}:{}@127.0.0.1:{}".format(
            self.rpc_user, self.rpc_password, self.rpc_port))
        self.connect.generate(101)
        print("[*]Generating blocks...")
        print("[*]Current balance for {} is {} BTC".format(self.rpc_user, self.check_balance()))

    def check_balance(self):
        balance = self.connect.getbalance()
        return balance/pow(10,8)

    def send_transaction(self, address, amount=100000):
        txid = self.connect.sendtoaddress(address,amount)

        print("[*]Transaction: {} ---> {} ({} BTC)\nTXID: {}".format(self.rpc_user, address, amount/pow(10,8), b2lx(txid)))

#Проверка на наличие аргумента пути к папкам узлов
if len(sys.argv) not in (2, 3):
    print("Error")
    sys.exit(1)

dir_el = os.listdir(sys.argv[1])
for el in dir_el:
    if el.startswith("node"):
        node_config = open("{}/{}/bitcoin.conf".format(sys.argv[1],el), "r")
        for string in node_config:
            if string.startswith("rpcuser"):
                rpc_user = string.split("=")[1]
                rpc_user = rpc_user[:len(rpc_user)-1]
            elif string.startswith("rpcpassword"):
                rpc_password = string.split("=")[1]
                rpc_password = rpc_password[:len(rpc_password)-1]
            elif string.startswith("rpcport"):
                rpc_port = string.split("=")[1]
                rpc_port = rpc_port[:len(rpc_port)-1]
        nodes.append(Node(rpc_user, rpc_password, rpc_port))


print("[*]Generator setup is complete\n"
      "[*]Was found {} nodes\n"
      "[*]Transaction formation begins...".format(str(len(nodes))))

while True:
    for node in nodes:
        recipients = list(nodes)
        recipients.remove(node)
        for recipient in recipients:
            rec_addr = recipient.connect.getnewaddress()
            node.send_transaction(rec_addr)