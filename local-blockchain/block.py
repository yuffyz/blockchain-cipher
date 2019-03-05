import datetime
from hashlib import sha256

"""
represent a block as objects 

pass trasactions and previous_hash to the default construct 
each time a Block is created 

"""
class Block:

  # initiate the object with properties
  def __init__(self, transactions, previous_hash, nonce = 0):

  	# the datestamp instance variable to store the current time
    self.timestamp = datetime.datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nounce = nounce
    self.hash = self.generate_hash()
    
  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
  # generate block hashes using 
  # the timestamp, data, and previous hash
  def generate_hash(self):

    # create a variable to be used to generate the hash
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
    
    # hash the contents
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()



