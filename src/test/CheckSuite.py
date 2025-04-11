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
        
    def test_411(self):
        """
            var a = [2] float {1, 2}
            var c [3] int = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],FloatType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3)]),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test_412(self):
        """
            type S1 struct {v int; x S1;}
            var b S1;
            var c = b.x.v;
            var d = c.x;
        """
        input = Program([StructType("S1",[("v",IntType()),("x",Id("S1"))],[]),VarDecl("b",Id("S1"), None),VarDecl("c", None,FieldAccess(FieldAccess(Id("b"),"x"),"v")),VarDecl("d", None,FieldAccess(Id("c"),"x"))])
        expect = "Type Mismatch: FieldAccess(Id(c),x)\n"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test_413(self):
        """
            func main() {
                a += 1
                var a int;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))), VarDecl("a", IntType(), None)]))])
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test_414(self):
        """
            var a boolean = 1 > 2;
            var b boolean = 1.0 < 2.0;
            var c boolean = "1" == "2";
            var d boolean = 1 > 2.0;
        """
        input = Program([VarDecl("a",BoolType(),BinaryOp(">", IntLiteral(1), IntLiteral(2))),VarDecl("b",BoolType(),BinaryOp("<", FloatLiteral(1.0), FloatLiteral(2.0))),VarDecl("c",BoolType(),BinaryOp("==", StringLiteral("1"), StringLiteral("2"))),VarDecl("d",BoolType(),BinaryOp(">", IntLiteral(1), FloatLiteral(2.0)))])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),>,FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test_415(self):
        """
            var a int = 1;
            var b int = 2;
            var c int = a + b;
            var d int = a + b + 1.0;
        """
        input = Program([VarDecl("a", IntType(), IntLiteral(1)), VarDecl("b", IntType(), IntLiteral(2)), VarDecl("c", IntType(), BinaryOp("+", Id("a"), Id("b"))), VarDecl("d", IntType(), BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), FloatLiteral(1.0)))])
        expect = "Type Mismatch: VarDecl(d,IntType,BinaryOp(BinaryOp(Id(a),+,Id(b)),+,FloatLiteral(1.0)))\n"
        self.assertTrue(TestChecker.test(input, expect, 415))
        
    def test_416(self):
        """
            func foo(){
                for var i int = 1; i < 10; i := 1.0 {
                    return;
                }
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),FloatLiteral(1.0)),Block([Return(None)]))]))])
        expect = "Type Mismatch: Assign(Id(i),FloatLiteral(1.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_417(self):
        """
            func foo(){
                var arr [2][3] int;
                for a, b := range arr {
                    var c int = a;
                    var d [3]int = b;
                    var e [2]string = a;
                }
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))]))]))])
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test_418(self):
        """
            func foo(a int) int {return 1;}

            var a int = foo(1 + 1);
            var b = foo(1.0);
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],IntType(),Block([Return(IntLiteral(1))])),VarDecl("a",IntType(),FuncCall("foo",[BinaryOp("+", IntLiteral(1), IntLiteral(1))])),VarDecl("b", None,FuncCall("foo",[FloatLiteral(1.0)]))])
        expect = "Type Mismatch: FuncCall(foo,[FloatLiteral(1.0)])\n"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test_419(self):
        """
            func foo() [2] float {
                return [2] float {1.0, 2.0};
                return [2] int {1, 2};
            }
        """
        input = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],FloatType()),Block([Return(ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])),Return(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        expect = "Type Mismatch: Return(ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test_420(self):
        """
            type Shape interface {
                calculate ();
                calculate (a int);
            }
        """
        input = Program([InterfaceType("Shape", [Prototype("calculate", [], VoidType()), Prototype("calculate", [("a", IntType())], VoidType())])])
        expect = "Redeclared Prototype: calculate\n"
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test_421(self):
        """
            func Haha (a, a int) {return;}
        """
        input = Program([FuncDecl("Haha", [ParamDecl("a", IntType()), ParamDecl("a", IntType())], VoidType(), Block([]))])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 421))
        
    def test_422(self):
        """
            func Foo () int {return 1;}

            func foo () {
                var b = Foo();
                foo_foo();
                return;
            }
        """
        input = Program([FuncDecl("Foo", [], IntType(), Block([Return(IntLiteral(1))])), FuncDecl("foo", [], VoidType(), Block([VarDecl("b", None, Id("Foo")), FuncCall("foo_foo", []), Return(None)]))])
        expect = "Undeclared Function: foo_foo\n"
        self.assertTrue(TestChecker.test(input, expect, 422))
        
    def test_423(self):
        """
            type BOOM struct {
                time int;
            }

            func (v BOOM) getInt () {
                const c = v.time;
                var d = v.size;
            }
        """
        input = Program([StructType("BOOM", [("time", IntType())], []), MethodDecl("v", Id("BOOM"), FuncDecl("getInt", [], VoidType(), Block([ConstDecl("c", None, FieldAccess(Id("v"), "time")), VarDecl("d", None, FieldAccess(Id("v"), "size"))])))])
        expect = "Undeclared Field: size\n"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test_424(self):
        """
            type A struct {x int;}
            type B struct {x int;}
            var a A;
            var b B = a;
        """
        input = Program([
            StructType("A", [("x", IntType())], []),
            StructType("B", [("x", IntType())], []),
            VarDecl("a", Id("A"), None),
            VarDecl("b", Id("B"), Id("a"))
        ])
        expect = "Type Mismatch: VarDecl(b,Id(B),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
    def test_425(self):
        """
            func test() int {
                return true;
            }
        """
        input = Program([
            FuncDecl("test", [], IntType(), Block([
                Return(BooleanLiteral(True))
            ]))
        ])
        expect = "Type Mismatch: Return(BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_426(self):
        """
            type X struct {
                a int;
                a float;
            }
        """
        input = Program([
            StructType("X", [("a", IntType()), ("a", FloatType())], [])
        ])
        expect = "Redeclared Field: a\n"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test_427(self):
        """
            func main() {
                var a = 1;
                a := "string";
            }
        """
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", None, IntLiteral(1)),
                Assign(Id("a"), StringLiteral("string"))
            ]))
        ])
        expect = """Type Mismatch: Assign(Id(a),StringLiteral(string))\n"""
        self.assertTrue(TestChecker.test(input, expect, 427))
        
    def test_428(self):
        """
            func main() {
                a := 1.0;
                var a float;
            }
        """
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), FloatLiteral(1.0)),
                VarDecl("a", FloatType(), None)
            ]))
        ])
        expect = """Redeclared Variable: a\n"""
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test_429(self):
        """
            func foo() int {
                const foo = 1;
                return foo()
            }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 429))
        
    def test_430(self):
        """
            var a int = 1 % 2;
            var b int = 1 % 2.0;
        """
        input = Program([VarDecl("a",IntType(),BinaryOp("%", IntLiteral(1), IntLiteral(2))),VarDecl("b",IntType(),BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test_431(self):
        """
            var a [2][3] int;
            var b = a[1];
            var c [3] int = b;
            var d [3] string = b;
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(3)],StringType()),Id("b"))])
        expect = "Type Mismatch: VarDecl(d,ArrayType(StringType,[IntLiteral(3)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test_432(self):
        """
            var A = 1;
            type A struct {a int;}
        """
        input = Program([VarDecl("A", None,IntLiteral(1)),StructType("A",[("a",IntType())],[])])
        expect = "Redeclared Type: A\n"
        self.assertTrue(TestChecker.test(input, expect, 432))
        
    def test_433(self):
        """
            type SMTH struct {a [2]int;} 

            func foo() SMTH {
                return nil
            }
        """
        input = Program([StructType("SMTH",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),FuncDecl("foo",[],Id("SMTH"),Block([Return(NilLiteral())]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))
        
    def test_434(self):
        """
            func foo(a [2] float) {
                foo([2] float {1.0,2.0})
                foo([2] int {1,2})
            }
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
        expect = "Type Mismatch: FuncCall(foo,[ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)])])\n"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        """
            func foo() {
                var a int = 1;
                var b float = a;
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(1)),VarDecl("b",FloatType(),Id("a"))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test_436(self):
        """
            type Person struct {
                name string ;
                age int ;
            }

            func  votien()  {
                var person = Person{name: "Alice", age: 30}
                person.name := "John";
                person.age := 30;
                putStringLn(person.name)
                putStringLn(person.Greet())
            }

            func (p Person) Greet() string {
                return "Hello, " + p.name
            }
        """
        input = Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),FuncDecl("votien",[],VoidType(),Block([VarDecl("person", None,StructLiteral("Person",[("name",StringLiteral("Alice")),("age",IntLiteral(30))])),Assign(FieldAccess(Id("person"),"name"),StringLiteral("John")),Assign(FieldAccess(Id("person"),"age"),IntLiteral(30)),FuncCall("putStringLn",[FieldAccess(Id("person"),"name")]),FuncCall("putStringLn",[MethCall(Id("person"),"Greet",[])])])),MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([Return(BinaryOp("+", StringLiteral("Hello, "), FieldAccess(Id("p"),"name")))])))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test_437(self):
        """
            type S1 struct {votien int;}
            type S2 struct {votien int;}
            type I1 interface {votien(e, e int) S1;}
            type I2 interface {votien(a int, b float) S1;}

            func (s S1) votien(a, b int) S1 {return s;}

            var a S1;
            var c I1 = a;
            var d I2 = a;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("votien",[IntType(),FloatType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("votien",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        expect = "Redeclared Method: votien\n"
        self.assertTrue(TestChecker.test(input, expect, 437))
        
    def test_438(self):
        """
            type WHAT struct {a [2]int;} 
            type WHY interface {foo() int;}

            func (v WHAT) foo() int {return 1;}

            func foo() {
                var b = WHAT{a: [2]int{1, 2}};
                var a int = b.a[1]
            }
        """
        input = Program([StructType("WHAT",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("WHY",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("WHAT"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,StructLiteral("WHAT",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),VarDecl("a",IntType(),ArrayCell(FieldAccess(Id("b"),"a"),[IntLiteral(1)]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test_439(self):
        """
            func foo() int {
                var a = 1;
                if (a < 3) {
                    var a = 1;
                } else if(a > 2) {
                    var a = 2;
                }
                return a;
            }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1)),If(BinaryOp("<", Id("a"), IntLiteral(3)), Block([VarDecl("a", None,IntLiteral(1))]), If(BinaryOp(">", Id("a"), IntLiteral(2)), Block([VarDecl("a", None,IntLiteral(2))]), None)),Return(Id("a"))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))
        
    def test_440(self):
        """
            func foo() {
                var a [5][6] int;
                var b [2] float;
                b[2] := a[2][3]
                a[2][3] := b[2] + 1;
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(5),IntLiteral(6)],IntType()), None),VarDecl("b",ArrayType([IntLiteral(2)],FloatType()), None),Assign(ArrayCell(Id("b"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]),BinaryOp("+", ArrayCell(Id("b"),[IntLiteral(2)]), IntLiteral(1)))]))])
        expect = "Type Mismatch: Assign(ArrayCell(Id(a),[IntLiteral(2),IntLiteral(3)]),BinaryOp(ArrayCell(Id(b),[IntLiteral(2)]),+,IntLiteral(1)))\n"
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_441(self):
        """
            type Person struct {
                name string;
                age  int;
            };
            func (p Person) getAge() int {
                p := Person{name: "Alice", age: 30}
                var q = Person{}
                return p.age
            };
        """
        input = Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),MethodDecl("p",Id("Person"),FuncDecl("getAge",[],IntType(),Block([Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral("Alice")),("age",IntLiteral(30))])),VarDecl("q", None,StructLiteral("Person",[])),Return(FieldAccess(Id("p"),"age"))])))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test_442(self):
        """
            var a = 1;
            func foo () {
                const b = 1;
                for a, c := range [3]int{1, 2, 3} {
                    var d = c;
                }
                var d = a;
                var a = 1;
            }
            var d = b;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("c"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("c"))])),VarDecl("d", None,Id("a")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("b"))])
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_443(self):
        """
            const v = 3;
            const k = v + 1;
            func foo(a [1 + 2] int) {
                foo([k - 1] int {1,2,3})
            } 
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("k",None,BinaryOp("+", Id("v"), IntLiteral(1))),FuncDecl("foo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_444(self):
        """
            type K struct {a int;}
            func (k K) koo(a [1 + 2] int) {return;}
            type H interface {koo(a [1 + 2] int);}

            const c = 4;
            func foo() {
                var k H;
                k.koo([c - 1] int {1,2,3})
            } 
        """
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],VoidType())]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],VoidType(),Block([VarDecl("k",Id("H"), None),MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))
        
    def test_445(self):
        """
            type K struct {a int;}
            func (k K) koo(a [1 + 2] int) [1 + 2] int {return [3*1] int {1,2,3};}
            type H interface {koo(a [1 + 2] int) [1 + 2] int;}

            const c = 4;
            func foo() [1 + 2] int{
                return foo()
                var k K;
                return k.koo([c - 1] int {1,2,3})
                var h H;
                return h.koo([c - 1] int {1,2,3})
            }   
        """
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(ArrayLiteral([BinaryOp("*", IntLiteral(3), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(FuncCall("foo",[])),VarDecl("k",Id("K"), None),Return(MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])),VarDecl("h",Id("H"), None),Return(MethCall(Id("h"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        """
            const a = 3;
            const b = -a;
            const c = -b;
            var d [c] int = [3] int {1,2,3}
        """
        input = Program([ConstDecl("a",None,IntLiteral(3)),ConstDecl("b",None,UnaryOp("-",Id("a"))),ConstDecl("c",None,UnaryOp("-",Id("b"))),VarDecl("d",ArrayType([Id("c")],IntType()),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test_447(self):
        """
            const a = 1;
            func foo() {
                a := 1.;
            }
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),FloatLiteral(1.0))]))])
        expect = "Type Mismatch: Assign(Id(a),FloatLiteral(1.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 447))
        
    def test_448(self):
        """
            func foo() {
                var a = 1.0 == 1
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,BinaryOp("==", FloatLiteral(1.0), IntLiteral(1)))]))])
        expect = "Type Mismatch: BinaryOp(FloatLiteral(1.0),==,IntLiteral(1))\n"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        """
            func foo() {
                foo := 1;
                foo()
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("foo"),IntLiteral(1)),FuncCall("foo",[])]))])
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test_450(self):
        """
            type Person stuct {
                name string;
                age int
            }
            func (p Person) Add(p int) {
                p.age := p.age + p
            }
        """
        input = Program([StructType("Person", [("name", StringType()), ("age", IntType())], []), MethodDecl("p", Id("Person"), FuncDecl("Add", [ParamDecl("p", IntType())], VoidType(), Block([Assign(FieldAccess(Id("p"), "age"), BinaryOp("+", FieldAccess(Id("p"), "age"), Id("p")))])))])
        expect = "Type Mismatch: FieldAccess(Id(p),age)\n"
        self.assertTrue(TestChecker.test(input, expect, 450))
        
    def test_451(self):
        """
            func foo () {
                var a = 1;
                var b = 1;
                for a, b := range [3]int {1, 2, 3} {
                    var b = 1;
                }
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1))]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test_452(self):
        """
            func foo(){
                var arr [2][3] int;
                var a = 1;
                var b[3]int;
                for a, b := range arr {
                    var c int = a;
                    var d [3]int = b;
                    var e [2]string = a;
                }
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("a", None,IntLiteral(1)),VarDecl("b",ArrayType([IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))]))]))])
        expect = "Type Mismatch: VarDecl(e,ArrayType(StringType,[IntLiteral(2)]),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 452))
        
    def test_453(self):
        """
            var v TIEN;      
            type TIEN struct {
                a int;
            } 
            type VO interface {
                fooA();
                fooB();
                fooC();
            }

            func (v TIEN) fooA() {return ;}
            func (foo TIEN) fooB() {
                foo()
                return ;
            }
            func (v TIEN) fooC()  {return ;}

            func foo() {
                var x VO = TIEN{a:1};  
            }
        """
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[]),InterfaceType("VO",[Prototype("fooA",[],VoidType()),Prototype("fooB",[],VoidType()),Prototype("fooC",[],VoidType())]),MethodDecl("v",Id("TIEN"),FuncDecl("fooA",[],VoidType(),Block([Return(None)]))),MethodDecl("foo",Id("TIEN"),FuncDecl("fooB",[],VoidType(),Block([FuncCall("foo",[]),Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("fooC",[],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("VO"),StructLiteral("TIEN",[("a",IntLiteral(1))]))]))])
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 453))
        
    def test_454(self):
        """
            func loop () {
                var array [2][3] int;
                var index int;
                var value [3] float;
                for index, value := range array {
                    return;
                }
            }
        """
        input = Program([FuncDecl("loop",[],VoidType(),Block([VarDecl("array",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("index",IntType(), None),VarDecl("value",ArrayType([IntLiteral(3)],FloatType()), None),ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))]))])
        expect = "Type Mismatch: ForEach(Id(index),Id(value),Id(array),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input, expect, 454))
        
    def test_455(self):
        """
            var v ABC;
            const b = v.b;        
            type ABC struct {
                a int;
                b int;
                c int;
            }
            const a = v.a;
            const e = v.e;
        """
        input = Program([VarDecl("v",Id("ABC"), None),ConstDecl("b",None,FieldAccess(Id("v"),"b")),StructType("ABC",[("a",IntType()),("b",IntType()),("c",IntType())],[]),ConstDecl("a",None,FieldAccess(Id("v"),"a")),ConstDecl("e",None,FieldAccess(Id("v"),"e"))])
        expect = "Undeclared Field: e\n"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_456(self):
        """
            var v TIEN;       
            type TIEN struct {
                a int;
            } 
            func (v TIEN) foo() int {return 1;}
            func (b TIEN) koo() {b.koo();}
            func foo() {
                const b = v.foo(); 
                v.koo(); 
                const d = v.zoo();
            }
        """
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,MethCall(Id("v"),"foo",[])),MethCall(Id("v"),"koo",[]),ConstDecl("d",None,MethCall(Id("v"),"zoo",[]))]))])
        expect = "Undeclared Method: zoo\n"
        self.assertTrue(TestChecker.test(input, expect, 456))
        
    def test_457(self):
        """
            func foo() int {return 1;}
            func  votien() int {
                return votien();
                foo();
            }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("votien",[],IntType(),Block([Return(FuncCall("votien",[])),FuncCall("foo",[])]))])
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        """
            type TIEN struct {v int;}
            var v TIEN;
            func foo(){
                for 1 {
                    var a int = 1.2;
                }
            }
        """
        input = Program([StructType("TIEN",[("v",IntType())],[]),VarDecl("v",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
        expect = "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.2))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test_459(self):
        """
            const v = 3;
            const a = v + v;
            var b [a * -(-2) + a] int;
            var c [18] int = b;
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), UnaryOp("-", UnaryOp("-", IntLiteral(2)))), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b"))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        """
            func loop (b int) {
                for var a = 1; c < 1; a += c {
                    const c = 2;
                }
            }
        """
        input = Program([FuncDecl("loop",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), Id("c"))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test_461(self):
        """
            func foo() {
                var a = foo
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,Id("foo"))]))])
        expect = "Undeclared Identifier: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
    def test_462(self):
        """
            type A struct { h int }
            func (a A) print() { return; }

            func main() {
                var b int;
                b.print();
            }
        """
        input = Program([StructType("A", [("h", IntType())], []), MethodDecl("a", Id("A"), FuncDecl("print", [], VoidType(), Block([Return(None)]))), FuncDecl("main", [], VoidType(), Block([VarDecl("b", IntType(), None), MethCall(Id("b"), "print", [])]))])
        expect = "Type Mismatch: MethodCall(Id(b),print,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
    def test_463(self):
        """
            type Node struct {
                next Node;
            }
        """
        input = Program([StructType("Node", [("next", Id("Node"))], [])])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test_464(self):
        """
            func main() {
                var x A;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", Id("A"), None)]))])
        expect = "Undeclared Type: A\n"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_465(self):
        """
            type A struct { h int }
            var a A = A{h:1};
        """
        input = Program([StructType("A", [("h", IntType())], []), VarDecl("a", Id("A"), StructLiteral("A", [("h", IntLiteral(1))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))
        
    def test_466(self):
        """
            func main() A {
                return A{h:1};
            }
        """
        input = Program([FuncDecl("main", [], Id("A"), Block([Return(StructLiteral("A", [("h", IntLiteral(1))]))]))])
        expect = "Undeclared Type: A\n"
        self.assertTrue(TestChecker.test(input, expect, 466))
        
    def test_467(self):
        """
            func printA() {
                return;
            }
            func main() {
                var a = printA();
            }
        """
        input = Program([FuncDecl("printA", [], VoidType(), Block([Return(None)])), FuncDecl("main", [], VoidType(), Block([VarDecl("a", None, FuncCall("printA", []))]))])
        expect = "Type Mismatch: FuncCall(printA,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 467))
        
    def test_468(self):
        """
            type TIEN struct {
                Votien int;
            }
            func (v TIEN) Votien () {return ;}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]), MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)])))])
        expect = "Redeclared Method: Votien\n"
        self.assertTrue(TestChecker.test(input, expect, 468))
        
    def test_469(self):
        """
            func (v HOW) putIntLn () {return;}
            func (v HOW) getInt () {return;}
            func (v HOW) getInt () {return;}
            type HOW struct {
                num int;
            }
        """
        input = Program([MethodDecl("v", Id("HOW"), FuncDecl("putIntLn", [], VoidType(), Block([Return(None)]))), MethodDecl("v", Id("HOW"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))), MethodDecl("v", Id("HOW"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))), StructType("HOW", [("Votien", IntType())], [])])
        expect = "Redeclared Method: getInt\n"
        self.assertTrue(TestChecker.test(input, expect, 469))
        
    def test_470(self):
        """
            type S1 struct {votien int;}
            type S2 struct {votien int;}
            type I1 interface {votien();}
            type I2 interface {votien();}

            func (s S1) votien() {return;}

            var a S1;
            var b S2;
            var c I1 = a;
            var d I2 = b;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),InterfaceType("I2",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        expect = "Redeclared Method: votien\n"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test_471(self):
        """
            type S1 struct {votien int;}
            type I1 interface {votien(a int) int;}
            func (s S1) votien( a int) int {return 1;}

            var s S1;
            var a int = s.votien(1);
            var b int = s.votien(1.0);
        """ 
        input = Program([StructType("S1",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[IntType()],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[ParamDecl("a",IntType())],IntType(),Block([Return(IntLiteral(1))]))),VarDecl("s",Id("S1"), None),VarDecl("a",IntType(),MethCall(Id("s"),"votien",[IntLiteral(1)])),VarDecl("b",IntType(),MethCall(Id("s"),"votien",[FloatLiteral(1.0)]))])
        expect = "Redeclared Method: votien\n"
        self.assertTrue(TestChecker.test(input, expect, 471))
        
    def test_472(self):
        """
            func main() {
                var arr [3]int;
                arr[3] := 5;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("arr", ArrayType([IntLiteral(3)], IntType()), None),Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(5))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
        
    def test_473(self):
        """
            func main() {
                var arr [3]string;
                arr[1] = 100;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("arr", ArrayType([IntLiteral(3)], StringType()), None), Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(100))]))])
        expect = "Type Mismatch: Assign(ArrayCell(Id(arr),[IntLiteral(1)]),IntLiteral(100))\n"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        """
            type A struct { x int; }
            func (a A) getX() int { return a.x; }
            func main() {
                var a A;
                var x int = a.getX(5);
            }
        """
        input = Program([StructType("A", [("x", IntType())], []), MethodDecl("a", Id("A"), FuncDecl("getX", [], IntType(), Block([Return(FieldAccess(Id("a"), "x"))]))), FuncDecl("main", [], VoidType(), Block([VarDecl("a", Id("A"), None), VarDecl("x", IntType(), MethCall(Id("a"), "getX", [IntLiteral(5)]))]))])
        expect = "Type Mismatch: MethodCall(Id(a),getX,[IntLiteral(5)])\n"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
    def test_475(self):
        """
            func main() {
                if true {
                    var x int = 5;
                }
                x := 10;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([If(BooleanLiteral(True), Block([VarDecl("x", IntType(), IntLiteral(5))]), None), Assign(Id("x"), IntLiteral(10))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test_476(self):
        """
            func add(a int, b int) int {
                return a + b;
            }

            func main() {
                var result = add(1, 2.0);
            }
        """
        input = Program([FuncDecl("add", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([Return(BinaryOp("+", Id("a"), Id("b")))])), FuncDecl("main", [], VoidType(), Block([VarDecl("result", None, FuncCall("add", [IntLiteral(1), FloatLiteral(2.0)]))]))])
        expect = "Type Mismatch: FuncCall(add,[IntLiteral(1),FloatLiteral(2.0)])\n"
        self.assertTrue(TestChecker.test(input, expect, 476))
        
    def test_477(self):
        """
            func foo() {
                return;
            }

            func bar() {
                foo(1);
            }
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([Return(None)])), FuncDecl("bar", [], VoidType(), Block([FuncCall("foo", [IntLiteral(1)])]))])
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(1)])\n"
        self.assertTrue(TestChecker.test(input, expect, 477))
        
    def test_478(self):
        """
            type A struct { x int; }
            func main() {
                var a A;
                var y = a.y;
            }
        """
        input = Program([StructType("A", [("x", IntType())], []), FuncDecl("main", [], VoidType(), Block([VarDecl("a", Id("A"), None), VarDecl("y", None, FieldAccess(Id("a"), "y"))]))])
        expect = "Undeclared Field: y\n"
        self.assertTrue(TestChecker.test(input, expect, 478))
        
    def test_479(self):
        """
            func foo() {
                var x = 1;
                x := 2.0;
            }
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([VarDecl("x", None, IntLiteral(1)), Assign(Id("x"), FloatLiteral(2.0))]))])
        expect = "Type Mismatch: Assign(Id(x),FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 479))
        
    def test_480(self):
        """
            func foo() {
                const foo = 1;
                var x = foo();
            }
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([ConstDecl("foo", None, IntLiteral(1)), VarDecl("x", None, FuncCall("foo", []))]))])
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        """
            func main() {
                var arr[5] int;
                var x = arr[true];
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None), VarDecl("x", None, ArrayCell(Id("arr"), [BooleanLiteral(True)]))]))])
        expect = "Type Mismatch: ArrayCell(Id(arr),[BooleanLiteral(true)])\n"
        self.assertTrue(TestChecker.test(input, expect, 481))
        
    def test_482(self):
        """
            type A struct { x int; }
            func main() {
                var a A;
                var y = a.x.y;
            }
        """
        input = Program([StructType("A", [("x", IntType())], []), FuncDecl("main", [], VoidType(), Block([VarDecl("a", Id("A"), None), VarDecl("y", None, FieldAccess(FieldAccess(Id("a"), "x"), "y"))]))])
        expect = "Type Mismatch: FieldAccess(FieldAccess(Id(a),x),y)\n"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        """
            func foo(a int, b int) int {
                return a + b;
            }

            func main() {
                var x = foo(1);
            }
        """
        input = Program([FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([Return(BinaryOp("+", Id("a"), Id("b")))])), FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, FuncCall("foo", [IntLiteral(1)]))]))])
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(1)])\n"
        self.assertTrue(TestChecker.test(input, expect, 483))
        
    def test_484(self):
        """
            type I interface { foo(); }
            type S struct { b int; }

            var a I = S;
        """
        input = Program([InterfaceType("I", [Prototype("foo", [], VoidType())]), StructType("S", [("b", IntType())], []), VarDecl("a", Id("I"), Id("S"))])
        expect = "Undeclared Identifier: S\n"
        self.assertTrue(TestChecker.test(input, expect, 484))
        
    def test_485(self):
        """
            type I interface { foo(); }
            type S struct { b int }

            func (s S) foo() {}

            var a I = S{b:1};
        """
        input = Program([InterfaceType("I", [Prototype("foo", [], VoidType())]), StructType("S", [("b", IntType())], []), MethodDecl("s", Id("S"), FuncDecl("foo", [], VoidType(), Block([Return(None)]))), VarDecl("a", Id("I"), StructLiteral("S", [("b", IntLiteral(1))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 485))
        
    def test_486(self):
        """
            func main() {
                var x = y + 1;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, BinaryOp("+", Id("y"), IntLiteral(1)))]))])
        expect = "Undeclared Identifier: y\n"
        self.assertTrue(TestChecker.test(input, expect, 486))
        
    def test_487(self):
        """
            func main() {
                for var i = 0; i < 10; i += 1 {
                    var i = 100;
                }
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([ForStep(VarDecl("i", None, IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([VarDecl("i", None, IntLiteral(100))]))]))])
        expect = "Redeclared Variable: i\n"
        self.assertTrue(TestChecker.test(input, expect, 487))
        
    def test_488(self):
        """
            func main() {
                var x = 1;
                var y = 2;
                var z = x + y;
                var t = x + y + z;
                var u = x + y + z + t;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, IntLiteral(1)), VarDecl("y", None, IntLiteral(2)), VarDecl("z", None, BinaryOp("+", Id("x"), Id("y"))), VarDecl("t", None, BinaryOp("+", BinaryOp("+", Id("x"), Id("y")), Id("z"))), VarDecl("u", None, BinaryOp("+", BinaryOp("+", BinaryOp("+", Id("x"), Id("y")), Id("z")), Id("t")))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))
        
    def test_489(self):
        """
            func foo() int {
                return;
            }
        """
        input = Program([FuncDecl("foo", [], IntType(), Block([Return(None)]))])
        expect = "Type Mismatch: Return()\n"
        self.assertTrue(TestChecker.test(input, expect, 489))
        
    def test_490(self):
        """
            func main() {
                for var i = 0; i < 5; i += 1 {
                    break;
                }
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([ForStep(VarDecl("i", None, IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(5)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([Break()]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))
        
    def test_491(self):
        """
            func main() {
                var x[3] int;
                var a = x[1.1];
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", ArrayType([IntLiteral(3)], IntType()), None), VarDecl("a", None, ArrayCell(Id("x"), [FloatLiteral(1.1)]))]))])
        expect = "Type Mismatch: ArrayCell(Id(x),[FloatLiteral(1.1)])\n"
        self.assertTrue(TestChecker.test(input, expect, 491))
        
    def test_492(self):
        """
            const a = 1 + 2;
            const b = 3 * (4 - 1);
            const c = -5;
            const d = +10;
            const e = !(true && false);
            const f = "Hello" + " World";
            const g = 1.5 * 2.0;
            const h = true || false;
            const i = 10 / 2 + 3;
            const num1 = b - (-c);
        """
        input = Program([ConstDecl("a", None, BinaryOp("+", IntLiteral(1), IntLiteral(2))), ConstDecl("b", None, BinaryOp("*", IntLiteral(3), BinaryOp("-", IntLiteral(4), IntLiteral(1)))), ConstDecl("c", None, UnaryOp("-", IntLiteral(5))), ConstDecl("d", None, UnaryOp("+", IntLiteral(10))), ConstDecl("e", None, UnaryOp("!", BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False)))), ConstDecl("f", None, BinaryOp("+", StringLiteral("Hello"), StringLiteral(" World"))), ConstDecl("g", None, BinaryOp("*", FloatLiteral(1.5), FloatLiteral(2.0))), ConstDecl("h", None, BinaryOp("||", BooleanLiteral(True), BooleanLiteral(False))), ConstDecl("i", None, BinaryOp("+", BinaryOp("/", IntLiteral(10), IntLiteral(2)), IntLiteral(3))), ConstDecl("num1", None, BinaryOp("-", Id("b"), UnaryOp("-", Id("c"))))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))
        
    def test_493(self):
        """
            func main() {
                var a int = 1;
                var b float = 2.0;
                a := b;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", None, IntLiteral(1)), VarDecl("b", None, FloatLiteral(2.0)), Assign(Id("a"), Id("b"))]))])
        expect = "Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 493))
        
    def test_494(self):
        """
            func main() {
                var x = x;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, Id("x"))]))])
        expect = "Undeclared Identifier: x\n"
        self.assertTrue(TestChecker.test(input, expect, 494))
        
    def test_495(self):
        """
            type A struct { x int; }
            func (a A) foo() int { return 1; }

            var x A;
            var y int = x.foo() + x.bar();
        """
        input = Program([StructType("A", [("x", IntType())], []), MethodDecl("a", Id("A"), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))), VarDecl("x", Id("A"), None), VarDecl("y", None, BinaryOp("+", MethCall(Id("x"), "foo", []), MethCall(Id("x"), "bar", [])))])
        expect = "Undeclared Method: bar\n"
        self.assertTrue(TestChecker.test(input, expect, 495))
        
    def test_496(self):
        """
            type A struct { x int; }
            func (a A) foo() int { return 1; }
            func (a A) bar() boolean { return false; }

            var x A;
            var y int = x.foo() + x.bar();
        """
        input = Program([StructType("A", [("x", IntType())], []), MethodDecl("a", Id("A"), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))), MethodDecl("a", Id("A"), FuncDecl("bar", [], BoolType(), Block([Return(BooleanLiteral(False))]))), VarDecl("x", Id("A"), None), VarDecl("y", None, BinaryOp("+", MethCall(Id("x"), "foo", []), MethCall(Id("x"), "bar", [])))])
        expect = "Type Mismatch: BinaryOp(MethodCall(Id(x),foo,[]),+,MethodCall(Id(x),bar,[]))\n"
        self.assertTrue(TestChecker.test(input, expect, 496))
        
    def test_497(self):
        """
            func lenString(string string) int {
                return 5;
            }
            
            var x int = lenString("Hello");
            var y = x && lenString("haha")
        """
        input = Program([FuncDecl("lenString", [ParamDecl("string", StringType())], IntType(), Block([Return(IntLiteral(5))])), VarDecl("x", None, FuncCall("lenString", [StringLiteral("Hello")])), VarDecl("y", None, BinaryOp("&&", Id("x"), FuncCall("lenString", [StringLiteral("haha")])))])
        expect = "Type Mismatch: BinaryOp(Id(x),&&,FuncCall(lenString,[StringLiteral(haha)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 497))
        
    def test_498(self):
        """
            func main() {
                var x = 1 % "a";
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, BinaryOp("%", IntLiteral(1), StringLiteral("a")))]))])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),%,StringLiteral(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 498))
        
    def test_499(self):
        """
            type A struct {}
            type B struct {}
            func (a A) foo() {}
            func (b B) foo() {}
        """
        input = Program([StructType("A", [], []), StructType("B", [], []), MethodDecl("a", Id("A"), FuncDecl("foo", [], VoidType(), Block([Return(None)]))), MethodDecl("b", Id("B"), FuncDecl("foo", [], VoidType(), Block([Return(None)])))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
        