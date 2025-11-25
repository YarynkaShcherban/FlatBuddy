import hashlib, json
from time import time
from typing import List, Dict

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(Block(0, time(), {"message": "Genesis Block"}, "0"))

    @property
    def last_block(self):
        return self.chain[-1]

    def add_record(self, data: Dict) -> Block:
        block = Block(
            index=len(self.chain),
            timestamp=time(),
            data=data,
            previous_hash=self.last_block.hash
        )
        self.chain.append(block)
        return block

blockchain = Blockchain()