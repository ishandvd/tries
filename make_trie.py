from treelib import Node, Tree

tree = Tree()

# A trie allows you to represent several strings in a compact form

# add a word letter by letter to a given point
# return current_id, which is the id of the last node added (the dollar sign)
def add_word(word, tree, prev_id, root_id):
    # get root of tree
    current_id = prev_id + 1
    for index, letter in enumerate(word):
        if index == 0:
            tree.create_node(word[0], current_id, parent=root_id)
        else:
            tree.create_node(word[index], current_id, parent=current_id-1)
        current_id += 1
    
    # Add dollar sign to end of word
    if len(word) == 0:
        tree.create_node("$", current_id, parent=root_id)
    else:
        tree.create_node("$", current_id, parent=current_id-1)
    
    return current_id


# find deepest match of word in tree
def find_deepest_match(word, tree):
    current_id = 0
    for index, letter in enumerate(word):
        # if letter exists in tree children, change current_id
        matches = [x.identifier for x in tree.children(current_id) if x.tag == letter]
        if len(matches) > 0:
            current_id = matches[0]
        else:
            return current_id, index
    
    return current_id, index + 1

# Root: Human readable identifier, id: internal identifier.
# We use ids starting from 0, and increment them as we add nodes
# ids help us to reference nodes in the tree
def make_trie(words):
    tree = Tree()
    current_id = 0
    tree.create_node("Root", current_id)

    for word in words:
        # figure out where to add the word
        deepest_match_id, deepest_match_index = find_deepest_match(word, tree)
        remaining_from_word = word[deepest_match_index:]
        current_id = add_word(remaining_from_word, tree, current_id, deepest_match_id)
    
    tree.show()
    return tree


# tree = make_trie(["hello", "hi","bye","byce", "world", "hell"])
# print("dummy")


def make_suffix_trie(genome):
    # add all suffixes of genome to trie
    trie = Tree()
    current_id = 0
    trie.create_node("Root", current_id)

    for i in range(len(genome)):
        suffix = genome[i:]
        # Find deepest match
        deepest_match_id, deepest_match_index = find_deepest_match(suffix, trie)
        remaining_from_word = suffix[deepest_match_index:]
        current_id = add_word(remaining_from_word, trie, current_id, deepest_match_id)
        current_id += 1
        trie.create_node(i, current_id, parent=current_id - 1)

    return trie

genome = "panamabananas"
trie = make_suffix_trie(genome)
trie.show()