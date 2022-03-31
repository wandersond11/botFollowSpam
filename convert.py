import re

arquivo = open(input("Chatterino Accounts: "),'r')
arquivo2 = open(input("New Text file: "),'w')

for linha in arquivo:
    x = re.split("[=|;|]",linha)
    print (f"oauth_token:{x[1]}:username:{x[3]}:user_id:{x[5]}:client_id:{x[7]}")
    arquivo2.write(f"oauth_token:{x[1]}:username:{x[3]}:user_id:{x[5]}:client_id:{x[7]}")


arquivo.close()
arquivo2.close()
