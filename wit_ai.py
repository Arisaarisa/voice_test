from wit import Wit

client = Wit('4DY5ZTXAIWGNGQS5GMTVVTH7UTGH5TFC')

resp = client.message('今何時ですか')
print('Yay, got Wit.ai response: ' + str(resp))
