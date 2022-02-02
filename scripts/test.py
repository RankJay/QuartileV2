from email.mime import image
import subprocess

imageURL = '''\\"https://bafybeiftczwrtyr3k7a2k4vutd3amkwsmaqyhrdzlhvpt33dyjivufqusq.ipfs.dweb.link/goteam-gif.gif\\"'''
royalty = [["benjiman.testnet", 2000], ["mike.testnet", 1000], ["josh.testnet", 500]]
royalties = '''{ '''
for entry in royalty:
    royalties = royalties + '''\\"''' + str(entry[0]) + '''\\":''' + str(entry[1]) + ''', '''

royalties = royalties[0:-2:1] + ''' }'''
# cmd = '''near call example-nft.testnet nft_mint "{\\"token_id\\": \\"fifthtryonnear\\", \\"receiver_id\\": \\"rankjay.testnet\\", \\"token_metadata\\": { \\"title\\": \\"NFT_TEST5\\", \\"description\\": \\"NFT on NEAR 1\\", \\"media\\": ''' + imageURL + ''', \\"copies\\": 1}}" --accountId rankjay.testnet --deposit 0.1'''
cmd = '''near call royalty.rankjay.testnet nft_mint "{\\"token_id\\": \\"sixthtryonnear\\", \\"metadata\\": {\\"title\\": \\"NFT_TEST6\\", \\"description\\": \\"testing out the new approval extension of the standard\\", \\"media\\": \\"https://bafybeiftczwrtyr3k7a2k4vutd3amkwsmaqyhrdzlhvpt33dyjivufqusq.ipfs.dweb.link/goteam-gif.gif\\"}, \\"receiver_id\\": \\"royalty.rankjay.testnet\\", \\"perpetual_royalties\\": ''' + royalties + '''}" --accountId royalty.rankjay.testnet --amount 0.1'''

print(cmd)
runOnCMD = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
print(runOnCMD)