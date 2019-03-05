"""
represent blockchain as an object
each participant could have their own instances 

properties:
chain
unverified transactions
genesis block

"""

#imports the Block class from block.py
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []

    # automatically create a Genesis Block
    # when a new blockchain object is created
    self.genesis_block()

  # the 1st block of the blockchain
  # with previous hash of 0
  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")

    # append the 1st block to the chain 
    self.chain.append(genesis_block)
    return self.chain

  # prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()    
  
  # add block to blockchain `chain`
  def add_block(self, transactions):

    # the previous block's hash could be created by 
    # accessing the previous block
    # and apply the generate_hash method on it
    previous_block_hash = self.chain[len(self.chain)-1].hash

    # create a new block that takes in a transaction
    # and the previous_hash
    new_block = Block(transactions, previous_block_hash)
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block)

    return proof, new_block

  # check to see if blocks are linked
  # to each other properly
  def validate_chain(self):

    # loop through each of the blocks
    # check if the previous hash value
    # match with the hash value inside previoss block    
    for i in range(1, len(self.chain)):

      current = self.chain[i]
      previous = self.chain[i-1]

      if(current.hash != current.generate_hash()):
        print("The current hash of the block does not equal the generated hash of the block.")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("The previous block's hash does not equal the previous hash value stored in the current block.")
        return False
    
    # if the two conditions are not satisfied 
    return True

    # solve this problem with 2 leading zeros
    def proof_of_work(self, block, difficulty=2):

      proof = block.generate_hash()

      # loop until the hash with the required difficulty is generated
      while (proof[:difficulty] != '0' * difficulty):
        block.nonce += 1
        proof = block.generate_hash()
      
      block.nonce = 0
      return proof


