"""
 * @author nhphung
"""
import sys
sys.path.append("/Users/peace/btl3-ppl")

from src.main.minigo.utils.AST import * 
from src.main.minigo.utils.Visitor import *
from src.main.minigo.utils.Utils import Utils
from StaticError import *
from functools import reduce
from typing import Tuple

class FunctionType(Type):
    def __str__(self):
        return "FunctionType"

    def accept(self, v, param):
        return v.visitFunctionType(self, v, param)


class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.list_function: List[FuncDecl] =  [
                FuncDecl("getInt", [], IntType(), Block([])),
                FuncDecl("putInt", [ParamDecl("i", IntType())], VoidType(), Block([])),
                FuncDecl("putIntLn", [ParamDecl("i", IntType())], VoidType(), Block([])),
                FuncDecl("getFloat", [], FloatType(), Block([])),
                FuncDecl("putFloat", [ParamDecl("f", FloatType())], VoidType(), Block([])),
                FuncDecl("putFloatLn", [ParamDecl("f", FloatType())], VoidType(), Block([])),
                FuncDecl("getString", [], StringType(), Block([])),
                FuncDecl("putString", [ParamDecl("s", StringType())], VoidType(), Block([])),
                FuncDecl("putStringLn", [ParamDecl("s", StringType())], VoidType(), Block([])),
                FuncDecl("getBool", [], BoolType(), Block([])),
                FuncDecl("putBool", [ParamDecl("b", BoolType())], VoidType(), Block([])),
                FuncDecl("putBoolLn", [ParamDecl("b", BoolType())], VoidType(), Block([])),
                FuncDecl("putLn", [], VoidType(), Block([]))
            ]
        self.function_current: FuncDecl = None

    def check(self):
        self.visit(self.ast, None)

    def checkType(self, LSH_type: Type, RHS_type: Type, list_type_permission: List[Tuple[Type, Type]] = []) -> bool:
        LSH_type = self.lookup(LSH_type.name, self.list_type, lambda x: x.name) if isinstance(LSH_type, Id) else LSH_type
        
        if type(RHS_type) == StructType and RHS_type.name == "":
            if type(LSH_type) == StructType or type(LSH_type) == InterfaceType:
                return True
                
        RHS_type = self.lookup(RHS_type.name, self.list_type, lambda x: x.name) if isinstance(RHS_type, Id) else RHS_type
                
        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                for method in LSH_type.methods:
                    struct_method = self.lookup(method.name, RHS_type.methods, lambda x: x.name)
                    
                    if struct_method is None:
                        return False
                    
                    param_types = [param.parType for param in struct_method.params]
                    
                    if type(method.retType) != type(struct_method.retType):
                        return False
                    
                    if len(method.params) != len(param_types):
                        return False
                    
                    for i in range(len(method.params)):
                        if type(method.params[i]) != type(param_types[i]):
                            return False
                    
                    if isinstance(method.retType, Id) and isinstance(struct_method.retType, Id):
                        if method.retType.name != struct_method.retType.name:
                            return False
                
            return True   
        
        if isinstance(LSH_type, (StructType, InterfaceType)) and isinstance(RHS_type, (StructType, InterfaceType)):
            return LSH_type.name == RHS_type.name

        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            lhs = self.lookup(LSH_type.eleType.name, self.list_type, lambda x: x.name) if isinstance(LSH_type.eleType, Id) else LSH_type
            if isinstance(lhs, InterfaceType):
                return False
            
            if LSH_type.dimens == RHS_type.dimens:
                if isinstance(LSH_type.eleType, FloatType) and isinstance(RHS_type.eleType, IntType):
                    return True
                else:
                    return type(LSH_type.eleType) == type(RHS_type.eleType)
            else:
                return False
            
        return type(LSH_type) == type(RHS_type)
    
    def evaluate_ast(self, node: AST, c : List[List[Symbol]]) -> int:
        if type(node) == IntLiteral:
            return int(node.value)
        elif type(node) == Id:
            res = next(filter(None, (self.lookup(node.name, scope, lambda x: x.name) for scope in c)), None)
            if res is None:
                raise Undeclared(Identifier(), node.name)
            
            return res.value
        elif isinstance(node, BinaryOp):
            left = self.evaluate_ast(node.left, c)
            right = self.evaluate_ast(node.right, c)
            
            if isinstance(left, IntLiteral):
                left = int(left.value)
                
            if isinstance(right, IntLiteral):
                right = int(right.value)
            
            if isinstance(left, int) and isinstance(right, int):
                if node.op in ['+', '-', '*', '/', '%']:
                    if node.op == '+':
                        return int(left + right)
                    elif node.op == '-':
                        return int(left - right)
                    elif node.op == '*':
                        return int(left * right)
                    elif node.op == '/':
                        if right == 0:
                            raise TypeMismatch(StaticErrorType())
                        return int(left / right)
                    elif node.op == '%':
                        return int(left % right)
        elif isinstance(node, UnaryOp):
            body = self.evaluate_ast(node.body, c)
            if isinstance(body, IntLiteral):
                body = int(body.value)
            if isinstance(body, int):
                if node.op == '+':
                    return int(body)
                if node.op == '-':
                    return int(-body)


    def visitProgram(self, ast: Program, c : None):
        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            if c is None:
                raise Undeclared(Type(), ast.recType.name)
            
            # check for each method
            existing_method = self.lookup(ast.fun.name, c.methods, lambda x: x.name)
            if existing_method:
                raise Redeclared(Method(), ast.fun.name)
            
            # check for comparing method and field
            existing_field = self.lookup(ast.fun.name, c.elements, lambda x: x[0])
            if existing_field:
                raise Redeclared(Method(), ast.fun.name)
            
            c.methods.append(ast.fun)
                        
            return ast
    
        list_str = ["getInt", "putInt", "putIntLn", "getFloat", "putFloat", "putFloatLn", "getString", "putString", "putStringLn", "getBool", "putBool", "putBoolLn", "putLn"]
        for item in ast.decl:
            if isinstance(item, Type):
                if item.name in list_str:
                    raise Redeclared(StaticError(), item.name)
                list_str.append(item.name)
            if isinstance(item, VarDecl):
                if item.varName in list_str:
                    raise Redeclared(Variable(), item.varName)
                list_str.append(item.varName)
            if isinstance(item, ConstDecl):
                if item.conName in list_str:
                    raise Redeclared(Constant(), item.conName)
                list_str.append(item.conName)
            if isinstance(item, FuncDecl):
                list_str.append(item.name)
            if isinstance(item, MethodDecl):
                list_str.append(item.fun.name)


        self.list_type = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc, ast.decl, [])
        self.list_function = self.list_function + list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))
        
        list(map(
            lambda item: visitMethodDecl(item, self.lookup(item.recType.name, self.list_type, lambda x: x.name)), 
             list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        ))
        
        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:], 
            filter(lambda item: isinstance(item, Decl), ast.decl), 
            [[
                Symbol("getInt", FunctionType()),
                Symbol("putInt", FunctionType()),
                Symbol("putIntLn", FunctionType()),
                Symbol("getFloat", FunctionType()),
                Symbol("putFloat", FunctionType()),
                Symbol("putFloatLn", FunctionType()),
                Symbol("getString", FunctionType()),
                Symbol("putString", FunctionType()),
                Symbol("putStringLn", FunctionType()),
                Symbol("getBool", FunctionType()),
                Symbol("putBool", FunctionType()),
                Symbol("putBoolLn", FunctionType()),
                Symbol("putLn", FunctionType())
            ]]
        ) 


    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        
        if res is not None:
            raise Redeclared(StaticError(), ast.name)
                        
        def visitElements(element: Tuple[str,Type], env: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            name, ele_type = element
            
            if self.lookup(name, env, lambda x: x[0]) is not None:
                raise Redeclared(Field(), name)
            
            if isinstance(ele_type, Id):
                if ele_type.name == ast.name:
                    pass
                else:
                    res = self.lookup(ele_type.name, c, lambda x: x[0])
                    if res is None:
                        raise Undeclared(StaticError(), ele_type.name)
            
            return element

        ast.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ast.elements , [])
                
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        ast.params = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.params, [])
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c : List[Union[StructType, InterfaceType]]) -> InterfaceType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticError(), ast.name)  
        ast.methods = reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast
    
    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        
        # Set the current function
        self.function_current = ast
                
        self.visit(ast.body, [list(reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.params, []))] + c)

        # Reset function_current after processing
        self.function_current = None
        return Symbol(ast.name, ast.retType, None)

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        res = self.lookup(ast.parName, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c : List[List[Symbol]]) -> None:
        new_scope = [[self.visitParamDecl(ParamDecl(ast.receiver, ast.recType), [])]]
        param_scope = [list(reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.fun.params, []))]
                
        self.function_current = ast.fun
        
        self.visitBlock(ast.fun.body, param_scope + new_scope + c)
        
        self.function_current = None
                
    def visitVarDecl(self, ast: VarDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        
        LHS_type = ast.varType if ast.varType else None
        RHS_type = self.visit(ast.varInit, c) if ast.varInit else None
                
        if isinstance(LHS_type, ArrayType):
            if isinstance(LHS_type.eleType, InterfaceType):
                raise TypeMismatch(ast)
            
            for i in range(len(LHS_type.dimens)):
                value = self.evaluate_ast(LHS_type.dimens[i], c)
                
                if isinstance(value, IntLiteral):
                    value = int(value.value)
                
                if not isinstance(value, int):
                    raise TypeMismatch(ast)
                LHS_type.dimens[i] = IntLiteral(value)
                
        if isinstance(RHS_type, ArrayType):
            for i in range(len(RHS_type.dimens)):
                value = self.evaluate_ast(RHS_type.dimens[i], c)
                
                if isinstance(value, IntLiteral):
                    value = int(value.value)
                
                if not isinstance(value, int):
                    raise TypeMismatch(ast)
                RHS_type.dimens[i] = IntLiteral(value)
                                
        value = None
        
        if RHS_type:
            if isinstance(ast.varInit, (BinaryOp, UnaryOp, IntLiteral, Id)):
                value = IntLiteral(self.evaluate_ast(ast.varInit, c)) if ast.varInit else None
                       
        if RHS_type is None:
            return Symbol(ast.varName, LHS_type, None)
        elif LHS_type is None:
            return Symbol(ast.varName, RHS_type, value)
        elif self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            return Symbol(ast.varName, LHS_type, value)
        raise TypeMismatch(ast)
        

    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName) 
        
        LHS_type = ast.conType if ast.conType else None
        RHS_type = self.visit(ast.iniExpr, c)
        
        value = None
        if isinstance(ast.iniExpr, (BinaryOp, UnaryOp, IntLiteral, Id)):
            value = IntLiteral(self.evaluate_ast(ast.iniExpr, c))
                    
        if LHS_type is None:
            return Symbol(ast.conName, RHS_type, value)
        raise TypeMismatch(ast)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        acc = [[]] + c 

        for ele in ast.member:
            result = self.visit(ele, (acc, True)) if isinstance(ele, (FuncCall, MethCall)) else self.visit(ele, acc)
            if isinstance(result, Symbol):
                acc[0] = [result] + acc[0]

    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]) -> None: 
        if not isinstance(self.visit(ast.cond, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None: 
        symbol = self.visit(ast.init, [[]] +  c)
        if not isinstance(self.visit(ast.cond, [[symbol]]), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block([ast.init] + [ast.upda] + ast.loop.member), c)
    
    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None: 
        type_array = self.visit(ast.arr, c)
        if not isinstance(type_array, ArrayType):
            raise TypeMismatch(ast)
        
        index_decl = VarDecl(ast.idx.name, IntType(), None)
        
        if len(type_array.dimens) == 1:
            value_type = type_array.eleType
        else:
            value_type = ArrayType(type_array.dimens[1:], type_array.eleType)
                
        value_decl = VarDecl(ast.value.name, value_type, None)

        self.visit(Block([index_decl, value_decl] + ast.loop.member), c)
    
    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        res = next(filter(None, (self.lookup(ast.name, scope, lambda x: x.name) for scope in c)), None)
        if res and not isinstance(res.mtype, Function):
            return res.mtype
        raise Undeclared(Identifier(), ast.name)
    
    def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c
            
        check_name_global = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if self.function_current:
            if check_name_global and check_name_global.name == self.function_current.name:
                local_scope = reduce(lambda x, y: x + y, c)
                    
                for sym in local_scope:
                    if sym.name == ast.funName:
                        if not isinstance(sym.mtype, FunctionType):
                            raise Undeclared(Function(), ast.funName)
                        else:
                            break
        
        res = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if res:
            if len(res.params) != len(ast.args):
                raise TypeMismatch(ast)
            
            for param, arg in zip(res.params, ast.args):
                arg_type = self.visit(arg, c)
                param_type = param.parType
                if isinstance(arg_type, (StringLiteral, IntLiteral, FloatLiteral, BooleanLiteral)):
                    arg_type = self.visit(arg_type, c)
                    
                if isinstance(arg_type, ArrayType):
                    for i in range(len(arg_type.dimens)):
                        value = self.evaluate_ast(arg_type.dimens[i], c)
                        
                        if isinstance(value, IntLiteral):
                            value = int(value.value)
                        
                        if not isinstance(value, int):
                            raise TypeMismatch(ast)
                        arg_type.dimens[i] = IntLiteral(value)
                        
                if isinstance(param_type, ArrayType):
                    for i in range(len(param_type.dimens)):
                        value = self.evaluate_ast(param_type.dimens[i], c)
                        
                        if isinstance(value, IntLiteral):
                            value = int(value.value)
                        
                        if not isinstance(value, int):
                            raise TypeMismatch(ast)
                        param_type.dimens[i] = IntLiteral(value)
                                            
                if isinstance(param_type, ArrayType) and isinstance(arg_type, ArrayType):
                    if arg_type.dimens == param_type.dimens:
                        # if arg type is float and param type is int then it will raise type mismatch
                        if isinstance(arg_type.eleType, FloatType) and isinstance(param_type.eleType, IntType):
                            raise TypeMismatch(ast)
                        elif type(arg_type.eleType) != type(param_type.eleType):
                            raise TypeMismatch(ast)
                    else:
                        raise TypeMismatch(ast)
                    
                if not self.checkType(param_type, arg_type, []):
                    raise TypeMismatch(ast)
                
            if is_stmt and not isinstance(res.retType, VoidType):
                raise TypeMismatch(ast)
            if not is_stmt and isinstance(res.retType, VoidType):
                raise TypeMismatch(ast)
            return res.retType
        raise Undeclared(Function(), ast.funName)

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        receiver_type = self.visit(ast.receiver, c)
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(receiver_type, Id) else receiver_type
                        
        if not isinstance(receiver_type, StructType):
            raise TypeMismatch(ast)
                
        res = self.lookup(ast.field, receiver_type.elements, lambda x: x[0])
        if res is None:
            raise Undeclared(Field(), ast.field)
        
        return res[1]

    def visitMethCall(self, ast: MethCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c
        receiver_type = self.visit(ast.receiver, c)
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(receiver_type, Id) else receiver_type
        if not isinstance(receiver_type, (StructType, InterfaceType)):
            raise TypeMismatch(ast)
        
        res = self.lookup(ast.metName, receiver_type.methods, lambda x: x.name) if isinstance(receiver_type, StructType) else self.lookup(ast.metName, receiver_type.methods, lambda x: x.name)
        if res:
            if type(receiver_type) == StructType:
                if len(res.params) != len(ast.args):
                    raise TypeMismatch(ast)
                for param, arg in zip(res.params, ast.args):
                    arg_type = self.visit(arg, c)
                    if type(param.parType) != type(arg_type):
                        raise TypeMismatch(ast)
                if is_stmt and not isinstance(res.retType, VoidType):
                    raise TypeMismatch(ast)
                if not is_stmt and isinstance(res.retType, VoidType):
                    raise TypeMismatch(ast)   
                return res.retType
            if type(receiver_type) == InterfaceType:
                if len(res.params) != len(ast.args):
                    raise TypeMismatch(ast)
                
                for param, arg in zip(res.params, ast.args):
                    arg_type = self.visit(arg, c)
                    if isinstance(arg_type, (StringLiteral, IntLiteral, FloatLiteral, BooleanLiteral)):
                        arg_type = self.visit(arg_type, c)
                    
                    if isinstance(arg_type, ArrayType):
                        for i in range(len(arg_type.dimens)):
                            value = self.evaluate_ast(arg_type.dimens[i], c)
                            
                            if isinstance(value, IntLiteral):
                                value = int(value.value)
                            
                            if not isinstance(value, int):
                                raise TypeMismatch(ast)
                            arg_type.dimens[i] = IntLiteral(value)
                        
                    if isinstance(param, ArrayType):
                        for i in range(len(param.dimens)):
                            value = self.evaluate_ast(param.dimens[i], c)
                            
                            if isinstance(value, IntLiteral):
                                value = int(value.value)
                            
                            if not isinstance(value, int):
                                raise TypeMismatch(ast)
                            param.dimens[i] = IntLiteral(value)
                                            
                    if isinstance(param, ArrayType) and isinstance(arg_type, ArrayType):
                        if arg_type.dimens == param.dimens:
                            # if arg type is float and param type is int then it will raise type mismatch
                            if isinstance(arg_type.eleType, FloatType) and isinstance(param.eleType, IntType):
                                raise TypeMismatch(ast)
                            elif type(arg_type.eleType) != type(param.eleType):
                                raise TypeMismatch(ast)
                        else:
                            raise TypeMismatch(ast)
                    
                    if not self.checkType(param, arg_type, []):
                        raise TypeMismatch(ast)
                
                if is_stmt and not isinstance(res.retType, VoidType):
                    raise TypeMismatch(ast)
                if not is_stmt and isinstance(res.retType, VoidType):
                    raise TypeMismatch(ast)   
                return res.retType
        raise Undeclared(Method(), ast.metName)
        

    def visitIntType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitFloatType(self, ast, c: List[List[Symbol]])-> Type: return ast
    def visitBoolType(self, ast, c: List[List[Symbol]])-> Type: return ast
    def visitStringType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitVoidType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
        for dimen in ast.dimens:
            value = self.evaluate_ast(dimen, c) if isinstance(dimen, (IntLiteral, Id, BinaryOp, UnaryOp)) else dimen
            if not isinstance(value, int):
                raise TypeMismatch(ast)
        
        list(map(lambda item: self.visit(item, c), ast.dimens))
        return ast
    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> None:
        if type(ast.lhs) is Id:
            res = next(filter(None, (self.lookup(ast.lhs.name, scope, lambda x: x.name) for scope in c)), None)
                        
            if res is None:
                return Symbol(ast.lhs.name, self.visit(ast.rhs, c), None)
        
        LHS_type = self.visit(ast.lhs, c)
        RHS_type = self.visit(ast.rhs, c)
        
        if isinstance(LHS_type, (IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral)):
            LHS_type = self.visit(LHS_type, c)
            
        if isinstance(RHS_type, (IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral)):
            RHS_type = self.visit(RHS_type, c)
                
        if isinstance(LHS_type, FloatType) and isinstance(RHS_type, IntType):
            return None
        
        if not self.checkType(LHS_type, RHS_type, [(InterfaceType, StructType)]):
            raise TypeMismatch(ast)
                        
    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None: 
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.thenStmt.member), c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)

    def visitContinue(self, ast, c: List[List[Symbol]]) -> None: return None
    def visitBreak(self, ast, c: List[List[Symbol]]) -> None: return None
    def visitReturn(self, ast: Return, c: List[List[Symbol]]) -> None: 
        expr = self.visit(ast.expr, c) if ast.expr else VoidType()
        if type(expr) == StructType and expr.name == "":
            if type(self.function_current.retType) != StructType or type(self.function_current.retType) == InterfaceType:
                return None
            
        current_func_type = self.function_current.retType
        if isinstance(expr, (StringLiteral, IntLiteral, FloatLiteral, BooleanLiteral)):
            expr = self.visit(expr, c)
            
        if isinstance(expr, ArrayType):
            for i in range(len(expr.dimens)):
                value = self.evaluate_ast(expr.dimens[i], c)
                
                if isinstance(value, IntLiteral):
                    value = int(value.value)
                
                if not isinstance(value, int):
                    raise TypeMismatch(ast)
                expr.dimens[i] = IntLiteral(value)
                
        if isinstance(current_func_type, ArrayType):
            for i in range(len(current_func_type.dimens)):
                value = self.evaluate_ast(current_func_type.dimens[i], c)
                
                if isinstance(value, IntLiteral):
                    value = int(value.value)
                
                if not isinstance(value, int):
                    raise TypeMismatch(ast)
                current_func_type.dimens[i] = IntLiteral(value)
                
        if isinstance(expr, ArrayType) and isinstance(current_func_type, ArrayType):
            if expr.dimens == current_func_type.dimens:
                # if arg type is float and param type is int then it will raise type mismatch
                if isinstance(expr.eleType, FloatType) and isinstance(current_func_type.eleType, IntType):
                    raise TypeMismatch(ast)
                elif type(expr.eleType) != type(self.function_current.retType.eleType):
                    raise TypeMismatch(ast)
            else:
                raise TypeMismatch(ast)
            
        if not self.checkType(expr, current_func_type):
            raise TypeMismatch(ast)
        return None
    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        LHS_type = self.visit(ast.left, c)
        RHS_type = self.visit(ast.right, c)

        if ast.op in ['+']:
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType), StringType]):
                if type(LHS_type) == StringType:
                    return StringType()
                elif type(LHS_type) == FloatType:
                    return FloatType()
                elif type(RHS_type) == FloatType:
                    return FloatType()
                elif type(LHS_type) == IntType:
                    return IntType()
                                
                    
        if ast.op in ['-', '*', '/']:
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType)]):
                if type(LHS_type) == FloatType:
                    return FloatType()
                elif type(RHS_type) == FloatType:
                    return FloatType()
                elif type(LHS_type) == IntType:
                    return IntType()
                    
        if ast.op in ['%']:
            if self.checkType(LHS_type, RHS_type, [IntType]):
                return IntType()
            
        if ast.op in ['&&', '||']:
            if self.checkType(LHS_type, RHS_type, [BoolType]):
                return BoolType()
            
        if ast.op in ['==', '!=']:
            if self.checkType(LHS_type, RHS_type, []):
                return BoolType()
            
        if ast.op in ['>', '>=', '<', '<=']:
            if isinstance(LHS_type, IntType) and isinstance(RHS_type, IntType):
                return BoolType()
            
            if isinstance(LHS_type, FloatType) and isinstance(RHS_type, FloatType):
                return BoolType()
            
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        unary_type = self.visit(ast.body, c)
                
        if ast.op == '-':
            if not isinstance(unary_type, (IntType, FloatType)):
                raise TypeMismatch(ast)
            return unary_type
            
        if ast.op == '!':
            if not isinstance(unary_type, BoolType):
                raise TypeMismatch(ast)
            return unary_type
    
    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        array_type = self.visit(ast.arr, c)
        if not isinstance(array_type, (ArrayType, ArrayLiteral)):
            raise TypeMismatch(ast)
               
        for dimen in array_type.dimens:
            value = self.evaluate_ast(dimen, c) if isinstance(dimen, (IntLiteral, Id, BinaryOp, UnaryOp)) else dimen
            if not isinstance(value, int):
                raise TypeMismatch(ast)
            
        if not all(map(lambda item: self.checkType(self.visit(item, c), IntType()), ast.idx)):
            raise TypeMismatch(ast)
        if len(array_type.dimens) == len(ast.idx):
            return array_type.eleType
        elif len(array_type.dimens) > len(ast.idx):
            return ArrayType(array_type.dimens[len(ast.idx):], array_type.eleType)
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast, c: List[List[Symbol]]) -> Type: return IntType()
    def visitFloatLiteral(self, ast, c: List[List[Symbol]]) -> Type: return FloatType()
    def visitBooleanLiteral(self, ast, c: List[List[Symbol]]) -> Type: return BoolType()
    def visitStringLiteral(self, ast, c: List[List[Symbol]]) -> Type: return StringType()
    def visitArrayLiteral(self, ast:ArrayLiteral , c: List[List[Symbol]]) -> Type:  
        def nested2recursive(dat: Union[Literal, list['NestedList']], c: List[List[Symbol]]):
            if isinstance(dat,list):
                list(map(lambda value: nested2recursive(value, c), dat))
            else:
                self.visit(dat, c)
        nested2recursive(ast.value, c)
        return ArrayType(ast.dimens, ast.eleType)
    def visitStructLiteral(self, ast:StructLiteral, c: List[List[Symbol]]) -> Type: 
        list(map(lambda value: self.visit(value[1], c), ast.elements))
        struct = self.lookup(ast.name, self.list_type, lambda x: x.name)
        if struct is None:
            raise Undeclared(StaticError(), ast.name)
        return StructType(ast.name, ast.elements, struct.methods)
    def visitNilLiteral(self, ast:NilLiteral, c: List[List[Symbol]]) -> Type: return StructType("", [], [])