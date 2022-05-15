from hedera import *
OPERATOR_ID = AccountId.fromString(input("Please input your operator ID. "))
OPERATOR_KEY = PrivateKey.fromString(input("Please input your operator key. "))
client = Client.forTestnet()
client.setOperator(OPERATOR_ID, OPERATOR_KEY)
opt = input("What would you like to do? (g)et a password or (a)dd a password? ")
if opt == "g":
  passwordID = input("Please input your password ID. ")
  print(FileContentsQuery().setKeys(OPERATOR_KEY.getPublicKey()).setFileId(FileId.fromString(passwordID)).execute(client).toStringUtf8())
else:
  passwordSTR = input("Password? ")
  transaction = FileCreateTransaction().setKeys(OPERATOR_KEY.getPublicKey()).setContents(passwordSTR).setMaxTransactionFee(Hbar(2)).execute(client)
  print(transaction.getReceipt(client).fileId.toString())
