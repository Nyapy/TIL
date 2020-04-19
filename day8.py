import hashlib

class blockchain :
    def __init__(self, data,previous_hash, nonce=0):
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()
        self.print_block()

    def print_block(self):
        # prints block contents
        print("data:", self.data)
        print("prevhash:", self.previous_hash)
        print("hash:", self.hash)

    def generate_hash(self):
        # hash the blocks contents
        block_contents = str(self.data) + str(self.previous_hash) + str(self.nonce)
        block_hash = hashlib.sha256(block_contents.encode())
        if not self.data == "Genesis Block":
            while block_hash.hexdigest()[:5]!= "00000":
                self.nonce += 1
                block_contents = str(self.data) + str(self.previous_hash) + str(self.nonce)
                block_hash = hashlib.sha256(block_contents.encode())
        return block_hash.hexdigest()



blockchains = [blockchain("Genesis Block","")]
cnt = 0
n = 5
while cnt < n-1:
    blockchains += [blockchain(cnt+1,blockchains[cnt].hash)]
    cnt += 1