if __name__ == "__main__":
    '''
    ref. https://docs.python.org/3/tutorial/datastructures.html#sets
    A set is an unordered collection with no duplicate elements
    '''
    set_seqs = set()
    set_seqs.add('test1')
    set_seqs.add('test2')
    print('set_seqs:', set_seqs)
    set_seqs.add('test1')
    print('set_seqs:', set_seqs)
    set_seqs.remove('test1')
    print('set_seqs:', set_seqs)
