import sys
sys.path.append("/Users/peace/btl3-ppl")

import unittest
from TestUtils import TestChecker
from src.main.minigo.utils.AST import *

class CheckSuite(unittest.TestCase):
    def test_400(self):
        """var a int; var b int; var a int; """
        input = Program([VarDecl("a", IntType(), None), VarDecl("b", IntType(), None), VarDecl("a", IntType(), None)])
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_401(self):
        """var a int = 1.2;"""
        input = Program([VarDecl("a", IntType(), FloatLiteral(1.2))])
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_402(self):
        """var a int = b;"""
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,402))
        
    def test_403(self):
        """
            var a int; 
            const a = 1;
        """
        input = Program([VarDecl("a", IntType(), None), ConstDecl("a", None, IntLiteral(1))])
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test_404(self):
        """
            func main() {
                a();
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("a", [])]))])
        expect = "Undeclared Function: a\n"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_405(self):
        """
            var a = 2.1;
            func main() {
                var c = a.b;
            }
        """
        input = Program([VarDecl("a", None, FloatLiteral(2.1)), FuncDecl("main", [], VoidType(), Block([VarDecl("c", None, FieldAccess(Id("a"), "b"))]))])
        expect = "Type Mismatch: FieldAccess(Id(a),b)\n"
        self.assertTrue(TestChecker.test(input, expect, 405))
        
    def test_406(self):
        """
            func main() {
                var c = a.b();
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("c", None, MethCall(Id("a"), "b", []))]))])
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test_407(self):
        """
            var getInt = 1;
        """
        input = Program([VarDecl("getInt", None, IntLiteral(1))])
        expect = "Redeclared Variable: getInt\n"
        self.assertTrue(TestChecker.test(input, expect, 407))
        
    def test_408(self):
        """
            var a = 1;
            var b = a;
            var c = d;
        """
        input = Program([VarDecl("a", None, IntLiteral(1)), VarDecl("b", None, Id("a")), VarDecl("c", None, Id("d"))])
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_409(self):
        """
            func main() {
                const b = 10;
            }
            func main(a int) int {
                return a;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([ConstDecl("b", None, IntLiteral(10))])), FuncDecl("main", [ParamDecl("a", IntType())], IntType(), Block([Return(Id("a"))]))])
        expect = "Redeclared Function: main\n"
        self.assertTrue(TestChecker.test(input, expect, 409))
        
    def test_410(self):
        """
            const a = 2;
            func foo () {
                const a = 1;
                for var a = 1; a < 1; b := 2 {
                    const b = 1;
                }
            }
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Block([ConstDecl("b",None,IntLiteral(1))]))]))])
        expect = "Redeclared Constant: b\n"
        self.assertTrue(TestChecker.test(input, expect, 410))
    
  