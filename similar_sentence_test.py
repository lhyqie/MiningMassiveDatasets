import unittest

from similar_sentence import editdistanceLessThanOne, levenshteinDistance

class TestSequenceFunctions(unittest.TestCase):
    def test_editdistanceLessThanOne(self):
        s1 = [1,2,3]
        s2 = [1,2,3]
        self.assertTrue(editdistanceLessThanOne(s1, s2))
        
        s1 = [1,2,3]
        s2 = [1,2,3,4]
        self.assertTrue(editdistanceLessThanOne(s1, s2))
        
        s1 = [1,2,3,4]
        s2 = [1,2,3]
        self.assertTrue(editdistanceLessThanOne(s1, s2))
        
        s1 = [1,2,3]
        s2 = [1,2,3,4,5]
        self.assertFalse(editdistanceLessThanOne(s1, s2))
        
        s1 = [1,2,3,4,5]
        s2 = [1,2,3]
        self.assertFalse(editdistanceLessThanOne(s1, s2))
        
        s1 = [1,2,3]
        s2 = [1,3,4]
        self.assertFalse(editdistanceLessThanOne(s1, s2))
        
        s1 = [1,3,4]
        s2 = [1,2,3]
        self.assertFalse(editdistanceLessThanOne(s1, s2))
        
        s1 = [1,2,3]
        s2 = [0,2,3]
        self.assertTrue(editdistanceLessThanOne(s1, s2))
        
        s1 = [1,3,3]
        s2 = [0,2,3]
        self.assertFalse(editdistanceLessThanOne(s1, s2))
        
        s1 = [36543, 2228, 897, 920, 11344]
        s2 = [36543, 2228, 8857, 24, 920, 11344]
        self.assertFalse(editdistanceLessThanOne(s1, s2))
        
        s1 = [308, 38, 2537, 376, 416, 1, 403, 5, 38, 649]
        s2 = [308, 38, 2537, 48, 376, 416, 1, 403, 5, 38, 649]
        self.assertTrue(editdistanceLessThanOne(s1, s2))
    
    def test_editdistance(self):
        s1 = [308, 38, 2537, 376, 416, 1, 403, 5, 38, 649]
        s2 = [308, 38, 2537, 48, 376, 416, 1, 403, 5, 38, 649]
        print levenshteinDistance(s2, s1)
        
        s1 = [68, 173, 1854, 6137, 45, 15124, 1657, 30, 288, 629]
        s2 = [68, 173, 1854, 6137, 45, 15124, 1657, 30, 508, 288, 629]
        print levenshteinDistance(s1, s2)
        
if __name__ == '__main__':
    unittest.main()
