import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])



    def test_empty_01(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.is_empty(), True)
    
    def test_empty_02(self):
        bst = BinarySearchTree()
        bst.insert(1)
        self.assertEqual(bst.is_empty(), False)


    
    def test_search_01(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        
        self.assertEqual(bst.search(50), True)
        
        
    def test_search_02(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        
        self.assertEqual(bst.search(80), True)
        
        
    def test_search_03(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        
        self.assertEqual(bst.search(110), False)
        
    
        
    def test_search_04(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        
        self.assertEqual(bst.search(50.0), True)
        
    
    def test_search_05(self):
        bst = BinarySearchTree()
        
        
        self.assertEqual(bst.search(50.0), False)
        
    
    def test_search_06(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        
        self.assertEqual(bst.search(-1), False)
    
    
    
    
    def test_insert_01(self):
        bst = BinarySearchTree()
        
        bst.insert(15)
        self.assertEqual(bst.root.data, None)
        bst.insert(15, 'min')

        self.assertEqual(bst.root.data, 'min')
    
    
    def test_insert_02(self):
        bst = BinarySearchTree()
        
        bst.insert('a')
        
        bst.insert('b')
        bst.insert('c')
        bst.insert('d')

        self.assertEqual(bst.root.key, 'a')
        
    def test_insert_03(self):
        bst = BinarySearchTree()
        
        bst.insert('a')
        bst.insert('b')
        bst.insert('c')
        bst.insert('d')

        self.assertEqual(bst.root.right.key, 'b')
    
    def test_insert_04(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15)
        bst.insert(35)
        bst.insert(90)
        bst.insert(90)
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        bst.insert(-3)
        bst.insert(-5)
        bst.insert(-1)
        
        
    def test_insert_05(self):
        bst = BinarySearchTree()
        
        bst.insert(-3)
        bst.insert(-5)
        bst.insert(-1)

        self.assertEqual(bst.root.right.key, -1)
        self.assertEqual(bst.root.left.key, -5)
    
    
    
    
    
    def test_min_01(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        
        self.assertEqual(bst.find_min(), (15, 'min'))
    
    
    def test_min_02(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        bst.insert(-1)
        
        self.assertEqual(bst.find_min(), (-1, None))
    
    
    def test_min_03(self):
        bst = BinarySearchTree()
        
        self.assertEqual(bst.find_min(), None)
    
    
   

    def test_max_01(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        
        self.assertEqual(bst.find_max(), (90, 'max'))
        
        
    def test_max_02(self):
        bst = BinarySearchTree()
        
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        bst.insert(90.01)
        
        self.assertEqual(bst.find_max(), (90.01, None))
        
    def test_max_03(self):
        bst = BinarySearchTree()
        
        self.assertEqual(bst.find_max(), None)



   
   
    def test_height_01(self):
        bst = BinarySearchTree()
        
        self.assertEqual(bst.tree_height(), None)
        
    
    def test_height_02(self):
        bst = BinarySearchTree()
        bst.insert(83)
        self.assertEqual(bst.tree_height(), 0)
   
    def test_height_03(self):
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        self.assertEqual(bst.tree_height(), 5)
    
    def test_height_04(self):
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        bst.insert(100)
        bst.insert(101)
        self.assertEqual(bst.tree_height(), 5)
        
        
    def test_height_05(self):
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        bst.insert(100)
        bst.insert(101)
        bst.insert(102)
        self.assertEqual(bst.tree_height(), 6)
        
        
        
    def test_inorder_01(self):
        bst = BinarySearchTree()
        
        self.assertEqual(bst.inorder_list(), []) 

    def test_inorder_02(self):
        bst = BinarySearchTree()
        bst.insert(78)
        self.assertEqual(bst.inorder_list(), [78])
        
    def test_inorder_03(self):
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        self.assertEqual(bst.inorder_list(), [15,30,32,35,37,40,50,60,70,75,78,80,83,90])    

    def test_inorder_04(self):
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        bst.insert(-5)
        bst.insert(0.1)
        self.assertEqual(bst.inorder_list(), [-5,0.1,15,30,32,35,37,40,50,60,70,75,78,80,83,90])  
    
    def test_inorder_05(self):
        bst = BinarySearchTree()
        bst.insert('g')
        bst.insert('h')
        bst.insert('i')
        bst.insert('j')
        bst.insert('k')
        bst.insert('l')
        bst.insert('m')
        
        bst.insert('a')
        bst.insert('b')
        bst.insert('c')
        bst.insert('d')
        bst.insert('e')
        bst.insert('f')


        self.assertEqual(bst.inorder_list(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']) 
     


     
    def test_preorder_01(self):
        bst = BinarySearchTree()
        
        self.assertEqual(bst.preorder_list(), [])    

    def test_preorder_02(self):
       bst = BinarySearchTree()
       bst.insert(80)
       self.assertEqual(bst.preorder_list(), [80]) 
       
    def test_preorder_03(self):
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        self.assertEqual(bst.preorder_list(), [50,40,30,15,35,32,37,70,60,75,90,80,78,83])
    
    def test_preorder_04(self):
        bst = BinarySearchTree()
        bst.insert('a')
        bst.insert('b')
        bst.insert('c')
        bst.insert('d')
        bst.insert('e')
        bst.insert('f')
        bst.insert('g')
        bst.insert('h')
        bst.insert('i')
        bst.insert('j')
        bst.insert('k')
        bst.insert('l')
        bst.insert('m')
        
        
        self.assertEqual(bst.preorder_list(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])    
        
        
        
    def test_levelorder_01(self):
        bst = BinarySearchTree()
        
        self.assertEqual(bst.level_order_list(), [])     
        
        
    def test_levelorder_02(self):
        bst = BinarySearchTree()
        bst.insert(80)
        self.assertEqual(bst.level_order_list(), [80])   
        
    def test_levelorder_03(self):
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(40)
        bst.insert(70)
        bst.insert(30)
        bst.insert(60)
        bst.insert(75)
        bst.insert(15)
        bst.insert(15, 'min')
        bst.insert(35)
        bst.insert(90)
        bst.insert(90, 'max')
        bst.insert(32)
        bst.insert(37)
        bst.insert(80)
        bst.insert(78)
        bst.insert(83)
        self.assertEqual(bst.level_order_list(), [50,40,70,30,60,75,15,35,90,32,37,80,78,83]) 
        
    def test_levelorder_04(self):
        bst = BinarySearchTree()
        bst.insert('a')
        bst.insert('b')
        bst.insert('c')
        bst.insert('d')
        bst.insert('e')
        bst.insert('f')
        bst.insert('g')
        bst.insert('h')
        bst.insert('i')
        bst.insert('j')
        bst.insert('k')
        bst.insert('l')
        bst.insert('m')
        
        
        self.assertEqual(bst.level_order_list(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])    



if __name__ == '__main__': 
    unittest.main()
