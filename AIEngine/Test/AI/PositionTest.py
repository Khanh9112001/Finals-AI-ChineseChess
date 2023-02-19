# this file to test FenUtils.py

import unittest
from Source.AI.Search import Search


class TestSearch(unittest.TestCase):

    def testTotalTraversedNode(self):
        fen = "rheakaehr/9/7c1/p1p1p1p1p/9/9/P1P1P1P1P/1C2C1H2/9/RcEAKAE1R b"
        depth = 1
        searchObj = Search(fen, depth)
        move = searchObj.search_root_negamax()
        self.assertTrue(searchObj.position.allNode == 38, "test1")

    def testTotalTraversedNode2(self):
        fen = "rheakaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C2C4/9/RHEAKAEHR b"
        depth = 1
        searchObj = Search(fen, depth)
        move = searchObj.search_root_negamax()
        self.assertTrue(searchObj.position.allNode == 45, "test2")

    def testTotalTraversedNode3(self):
        fen = "rheakaehr/9/1c5c1/pCp1p1p1p/9/9/P1P1P1P1P/7C1/9/RHEAKAEHR b"
        depth = 1
        searchObj = Search(fen, depth)
        move = searchObj.search_root_negamax()
        self.assertTrue(searchObj.position.allNode == 40, "test3")

    def testTotalTraversedNode4(self):
        fen = "rheakaehr/9/1c5c1/pCp1p1p1p/9/9/P1P1P1P1P/7C1/9/RHEAKAEHR b"
        depth = 1
        searchObj = Search(fen, depth)
        move = searchObj.search_root_negamax()
        self.assertTrue(searchObj.position.allNode == 40, "test4")



if __name__ == '__main__':
    unittest.main()
