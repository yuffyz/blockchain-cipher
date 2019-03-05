"""
a script to change a block in the chain
and then check
"""

from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# Instantiate a new Blockchain object 
my_blockchain = Blockchain()

# add a new block and pass the transcation data
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()

# change the transcation of block 1 in the chain
my_blockchain.chain[1].transactions = "fake_transactions"

# check
my_blockchain.validate_chain()