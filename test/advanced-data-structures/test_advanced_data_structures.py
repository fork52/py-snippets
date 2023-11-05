from py_snippets.advanced_data_structures.segTree import MaxSegmentTree

def test_rangeQuery():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree = MaxSegmentTree(0, len(arr) - 1, arr)

    assert tree.rangeQuery(0, 2) == 3
    assert tree.rangeQuery(0, len(arr) - 1) == 10

def test_pointUpdate():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree = MaxSegmentTree(0, len(arr) - 1, arr)
    tree.pointUpdate(100, 0)
    assert tree.rangeQuery(0, 0) == 100