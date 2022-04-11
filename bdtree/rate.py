import json
import logging


class TreeParser():
    decision = []

    """Docstring for TreeParser. """

    def __init__(self, file_path: str = ""):
        f = open(file_path)
        self.tree = json.load(f)

    def decide(self, object):
        return self.decideNextNodeBSC(object, self.tree)

    def decideNextNodeBSC(self, object, nodes: dict):
        '''
        Start BSC recursion in the tree.

                Parameters:
                        node (dict): decision tree node
                        object (dict): Object to mach
                Returns:
                        decision (list): list of decisions meet in tree
        '''
        for node in nodes['children']:
            if 'children' not in node.keys():
                self.decision.append(node)
                break
            if self.computeCondition(node, object):
                self.decideNextNodeBSC(object, node)
        return self.decision

    def computeCondition(self, node: dict, object: dict) -> bool:
        '''
        Returns evals of the condition in the three.

                Parameters:
                        node (dict): decision tree node
                        object (dict): Object to mach
                Returns:
                        condition_result (bool): il condition in node is mached
                        by value in object
        '''
        condition_result = False
        operator = node['condition']
        y = node['value']
        x = object[node['name']]
        if operator == 'beetween':
            condition_result = eval(f'{y[0]} <= {x} <= {y[1]}')
            print(f"{x} {operator} {y} {condition_result}")
        else:
            condition_result = eval(f"{x} {operator} {y}")
            print(f"{x} {operator} {y} {condition_result}")
        return condition_result


tree = TreeParser()
print(tree.decide(
    {
        'category': 'veicolo-leggero',
        'km': 20,
        'day': 4
    }))
