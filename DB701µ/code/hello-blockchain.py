# hello-blockchain.py
# Author: Sébastien Combéfis
# Version: April 23, 2020

class Block:
    def __init__(self, index, timestamp, prevHash, data):
        pass

    def __str__(self):
        pass


class GenesisBlock(Block):
    def __init__(self, index, timestamp, data):
        super().__init__(index, timestamp, None, data)


class BlockChain:
    def __init__(self, name):
        self.name = name
        self.blocks = []

    def append(self, data):
        '''Add a new piece of data in this blockchain.'''
        pass

    def isValid(self):
        '''Checks whether this blockchain is valid.'''
        pass

    def __len__(self):
        return len(self.blocks)

    def __getitem__(self, i):
        return self.blocks[i]

    def __str__(self):
        pass


if __name__ == '__main__':
    blockchain = BlockChain('CombéCoin')
    print(blockchain)

    for block in blockchain:
        print(block)
