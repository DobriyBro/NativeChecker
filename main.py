from web3 import Web3

my_file = open("Result.txt", "w+")
file1 = open("address.txt", "r")
a = 1
my_file.write("________________________________________________________________________________________________________________________")
my_file.write("\n")
c = len(open('address.txt').readlines())
while True:

    wallet_address = file1.readline()

    wallet_address = wallet_address.replace("\n","")

    if not wallet_address:
        break


    checksum_address = Web3.to_checksum_address(wallet_address)

    def bsc(a):
        nbsc = "https://bsc-dataseed1.binance.org"
        web3 = Web3(Web3.HTTPProvider(nbsc))
        balance = web3.eth.get_balance(a)
        ether_balance = Web3.from_wei(balance, 'ether')
        return(f"\nBSC: {ether_balance} BNB")
    def eth(a):
        nbsc = "https://eth.llamarpc.com"
        web3 = Web3(Web3.HTTPProvider(nbsc))
        balance = web3.eth.get_balance(a)
        ether_balance = Web3.from_wei(balance, 'ether')
        return(f"\nETH: {ether_balance} ETH")
    def ARB(a):
        nbsc = "https://arb1.croswap.com/rpc"
        web3 = Web3(Web3.HTTPProvider(nbsc))
        balance = web3.eth.get_balance(a)
        ether_balance = Web3.from_wei(balance, 'ether')
        return(f"\nARBITRUM: {ether_balance} ETH")
    def POL(a):
        nbsc = "https://polygon.llamarpc.com"
        web3 = Web3(Web3.HTTPProvider(nbsc))
        balance = web3.eth.get_balance(a)
        ether_balance = Web3.from_wei(balance, 'ether')
        return(f"\nPOLIGON: {ether_balance} MATIC")
    def OP(a):
        nbsc = "https://mainnet.optimism.io"
        web3 = Web3(Web3.HTTPProvider(nbsc))
        balance = web3.eth.get_balance(a)
        ether_balance = Web3.from_wei(balance, 'ether')
        return(f"\nOPTIMISM: {ether_balance} ETH")
    def AVAX(a):
        nbsc = "https://avalanche.blockpi.network/v1/rpc/public"
        web3 = Web3(Web3.HTTPProvider(nbsc))
        balance = web3.eth.get_balance(a)
        ether_balance = Web3.from_wei(balance, 'ether')
        return(f"\nAVALANCHE: {ether_balance} AVAX")

    my_file.write(str(a))
    my_file.write(":")
    my_file.write("                              ")
    my_file.write(wallet_address)
    my_file.write("\n")
    my_file.write(bsc(checksum_address))
    my_file.write(eth(checksum_address))
    my_file.write(ARB(checksum_address))
    my_file.write(POL(checksum_address))
    my_file.write(OP(checksum_address))
    my_file.write(AVAX(checksum_address))
    my_file.write("\n")
    my_file.write("________________________________________________________________________________________________________________________")
    my_file.write("\n")
    print (a,"/",c)
    a = a + 1




file1.close
my_file.close()
print("Успешно! Можете закрывать консоль!")
c = input()