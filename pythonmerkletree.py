import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.leaf_nodes = [hashlib.sha256(str(tx).encode()).hexdigest() for tx in transactions]
        self.parents = []

    def build(self):
        if len(self.leaf_nodes) % 2 == 1:
            self.leaf_nodes.append(self.leaf_nodes[-1])

        while len(self.leaf_nodes) > 1:
            curr_parents = []
            for i in range(0, len(self.leaf_nodes), 2):
                curr_parents.append(hashlib.sha256(str(self.leaf_nodes[i] + self.leaf_nodes[i+1]).encode()).hexdigest())
            self.parents = curr_parents
            self.leaf_nodes = self.parents

if __name__ == '__main__':
    transactions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    merkle_tree = MerkleTree(transactions)
    merkle_tree.build()
    print(merkle_tree.parents)
