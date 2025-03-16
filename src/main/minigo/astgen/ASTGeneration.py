# import sys
# sys.path.append("/Users/peace/btl2-ppl")

from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

def getPrimitiveType(type):
    if type == "int":
        return IntType()
    elif type == "float":
        return FloatType()
    elif type == "string":
        return StringType()
    elif type == "boolean":
        return BoolType()
    return None
        
def getIntLiteral(ctx):
    num = ctx.INT_LITERALS().getText()
    if num.startswith("0x") or num.startswith("0X"):
        return IntLiteral(int(num, 16))
    elif num.startswith("0o") or num.startswith("0O"):
        return IntLiteral(int(num, 8))
    elif num.startswith("0b") or num.startswith("0B"):
        return IntLiteral(int(num, 2))
    return IntLiteral(int(num))

def getFloatLiteral(ctx):    
    return FloatLiteral(float(ctx.FLOAT_LITERALS().getText()))

def getStringLiteral(ctx):
    return StringLiteral(ctx.STRING_LITERALS().getText())

def getBooleanLiteral(ctx):
    return BooleanLiteral(ctx.BOOLEAN_LITERALS().getText() == "true")
        
class ASTGeneration(MiniGoVisitor):
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(i) for i in ctx.decl()])

    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))

    # func decl
    def visitFuncdecl(self,ctx:MiniGoParser.FuncdeclContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.funcParams()) if ctx.funcParams() else []
        retType = self.visit(ctx.funcType()) if ctx.funcType() else VoidType()
        block = [self.visit(i) for i in ctx.block()]
        if ctx.receiver():
            recName, recType = self.visit(ctx.receiver())
            return MethodDecl(recName, recType, FuncDecl(name, params, retType, Block(block)))
        return FuncDecl(name,params,retType,Block(block))
    
    # receiver for method
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        recName = ctx.ID(0).getText()
        recType = Id(ctx.ID(1).getText())
        return recName, recType
    
    def visitFuncType(self, ctx:MiniGoParser.FuncTypeContext):
        if ctx.PRIMITIVE_TYPE():
            return getPrimitiveType(ctx.PRIMITIVE_TYPE().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arrays_type():
            dimens, eleType = self.visit(ctx.arrays_type())
            return ArrayType(dimens, eleType)
        
    def visitFuncParams(self, ctx:MiniGoParser.FuncParamsContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.funcParam()) + self.visit(ctx.funcParams())
        return self.visit(ctx.funcParam())
        
    def visitFuncParam(self, ctx:MiniGoParser.FuncParamContext):
        return [ParamDecl(name, self.visit(ctx.funcType())) for name in self.visit(ctx.funcListName())]
        
    def visitFuncListName(self, ctx:MiniGoParser.FuncListNameContext):
        if ctx.getChildCount() == 3:
            return [ctx.ID().getText()] + self.visit(ctx.funcListName())
        return [ctx.ID().getText()]
    
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl())
        elif ctx.shortvardecl():
            return self.visit(ctx.shortvardecl())
        elif ctx.returndecl():
            return self.visit(ctx.returndecl())
        elif ctx.ifelsedecl():
            return self.visit(ctx.ifelsedecl())
        elif ctx.forloopdecl():
            return self.visit(ctx.forloopdecl())
        elif ctx.access_field():
            return self.visit(ctx.access_field())
        elif ctx.funcdecl():
            return self.visit(ctx.funcdecl())
    
    # var decl	
    def visitVardecl(self,ctx:MiniGoParser.VardeclContext):
        varName = ctx.ID().getText()
        varType = self.visit(ctx.varType()) if ctx.varType() else None
        varInit = self.visit(ctx.value_assign()) if ctx.value_assign() else None
        return VarDecl(varName,varType,varInit)
    
    # const decl
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        conName = ctx.ID().getText()
        iniExpr = self.visit(ctx.value_assign())
        return ConstDecl(conName, None, iniExpr)
    
    # assign decl
    def visitShortvardecl(self, ctx:MiniGoParser.ShortvardeclContext):
        lhs = self.visit(ctx.lhs())
        op = self.visit(ctx.assign_operators())
        rhs = BinaryOp(op, lhs, self.visit(ctx.value_assign())) if op else self.visit(ctx.value_assign())
        return Assign(lhs, rhs)
    
    # for loop decl
    def visitForloopdecl(self, ctx:MiniGoParser.ForloopdeclContext):
        if ctx.initialization() and ctx.condition() and ctx.update():
            init = self.visit(ctx.initialization())
            cond = self.visit(ctx.condition())
            upda = self.visit(ctx.update())
            loop = Block([self.visit(block) for block in ctx.block_inside_loop()])
            return ForStep(init, cond, upda, loop)
        elif ctx.for_access_value():
            idx = self.visit(ctx.for_access_value(0))
            value = self.visit(ctx.for_access_value(1))
            arr = self.visit(ctx.for_arr())
            loop = Block([self.visit(block) for block in ctx.block_inside_loop()])
            return ForEach(idx, value, arr, loop)
        return ForBasic(self.visit(ctx.condition()), Block([self.visit(block) for block in ctx.block_inside_loop()]))
    
    # initialization
    def visitInitialization(self, ctx:MiniGoParser.InitializationContext):
        return Assign(Id(ctx.ID().getText()), self.visit(ctx.value_assign()))
    
    # condition
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visit(ctx.expression_boolean())
    
    # update
    def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
        lhs = Id(ctx.ID().getText())
        op = self.visit(ctx.other_operations())
        rhs = BinaryOp(op, lhs, self.visit(ctx.value_assign()))
        return Assign(lhs, rhs)
    
    def visitFor_access_value(self, ctx:MiniGoParser.For_access_valueContext):
        return Id(ctx.getChild(0).getText())
    
    def visitFor_arr(self, ctx:MiniGoParser.For_arrContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.expression_array():
            return self.visit(ctx.expression_array())
        elif ctx.access_field():
            return self.visit(ctx.access_field())
        
    def visitBlock_inside_loop(self, ctx:MiniGoParser.Block_inside_loopContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl())
        elif ctx.shortvardecl():
            return self.visit(ctx.shortvardecl())
        elif ctx.ifelsedecl_inside_loop():
            return self.visit(ctx.ifelsedecl_inside_loop())
        elif ctx.returndecl():
            return self.visit(ctx.returndecl())
        elif ctx.breakdecl():
            return self.visit(ctx.breakdecl())
        elif ctx.continuedecl():
            return self.visit(ctx.continuedecl())
        elif ctx.forloopdecl():
            return self.visit(ctx.forloopdecl())
        elif ctx.access_field():
            return self.visit(ctx.access_field())
        
    # if else decl
    def visitIfelsedecl(self, ctx:MiniGoParser.IfelsedeclContext):
        expr = self.visit(ctx.expression_boolean())
        thenStmt = Block([self.visit(block) for block in ctx.block()])
        elseStmt = None
        if ctx.elifdecls():
            elifdecls = self.visit(ctx.elifdecls())
            for e in elifdecls:
                elif_expr, elif_then = e
                elseStmt = If(elif_expr, elif_then, elseStmt)
            if ctx.elsedecl():
                finalElse = self.visit(ctx.elsedecl())
                elseStmt = If(elif_expr, elif_then, finalElse)
        elif ctx.elsedecl():
            elseStmt = self.visit(ctx.elsedecl())
        return If(expr, thenStmt, elseStmt)
    
    def visitElifdecls(self, ctx:MiniGoParser.ElifdeclsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.elifdecl())] + self.visit(ctx.elifdecls())
        return [self.visit(ctx.elifdecl())]
    
    def visitElifdecl(self, ctx:MiniGoParser.ElifdeclContext):
        elif_expr = self.visit(ctx.expression_boolean())
        elif_then = Block([self.visit(block) for block in ctx.block()])
        return (elif_expr, elif_then)
    
    def visitElsedecl(self, ctx:MiniGoParser.ElsedeclContext):
        return Block([self.visit(block) for block in ctx.block()])
    
    # if else inside a loop
    def visitIfelsedecl_inside_loop(self, ctx:MiniGoParser.Ifelsedecl_inside_loopContext):
        expr = self.visit(ctx.expression_boolean())
        thenStmt = Block([self.visit(block) for block in ctx.block_inside_loop()])
        elseStmt = None
        if ctx.elifdecls_inside_loop():
            elifdecls = self.visit(ctx.elifdecls_inside_loop())
            for e in elifdecls:
                elif_expr, elif_then = e
                elseStmt = If(elif_expr, elif_then, elseStmt)
            if ctx.elsedecl_inside_loop():
                finalElse = self.visit(ctx.elsedecl_inside_loop())
                elseStmt = If(elif_expr, elif_then, finalElse)
        elif ctx.elsedecl_inside_loop():
            elseStmt = self.visit(ctx.elsedecl_inside_loop())
        return If(expr, thenStmt, elseStmt)
    
    def visitElifdecls_inside_loop(self, ctx:MiniGoParser.Elifdecls_inside_loopContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.elifdecl_inside_loop())] + self.visit(ctx.elifdecls_inside_loop())
        return [self.visit(ctx.elifdecl_inside_loop())]
    
    def visitElifdecl_inside_loop(self, ctx:MiniGoParser.Elifdecl_inside_loopContext):
        elif_expr = self.visit(ctx.expression_boolean())
        elif_then = Block([self.visit(block) for block in ctx.block_inside_loop()])
        return (elif_expr, elif_then)
    
    def visitElsedecl_inside_loop(self, ctx:MiniGoParser.Elsedecl_inside_loopContext):
        return Block([self.visit(block) for block in ctx.block_inside_loop()])
    
    # assign operators :=, +=, -=, *=, /=, %=
    def visitAssign_operators(self, ctx:MiniGoParser.Assign_operatorsContext):
        return self.visit(ctx.other_operations()) if ctx.other_operations() else None
    
    def visitOther_operations(self, ctx:MiniGoParser.Other_operationsContext):
        if ctx.PLUS_EQUAL():
            return "+"
        elif ctx.MINUS_EQUAL():
            return "-"
        elif ctx.MULTIPLY_EQUAL():
            return "*"
        elif ctx.DIVIDE_EQUAL():
            return "/"
        elif ctx.MODULO_EQUAL():
            return "%"
    
    # left-hand-side
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.access_field():
            return self.visit(ctx.access_field())
        
    def visitVarType(self, ctx:MiniGoParser.VarTypeContext):
        if ctx.PRIMITIVE_TYPE():
            return getPrimitiveType(ctx.PRIMITIVE_TYPE().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arrays_type():
            dimens, eleType = self.visit(ctx.arrays_type())
            return ArrayType(dimens, eleType)
        
    # access field for right-hand-side    
    def visitAccess_field(self, ctx:MiniGoParser.Access_fieldContext):
        if ctx.field() and ctx.access_field():
            right = self.visit(ctx.field())
            left = self.visit(ctx.access_field())
            if ctx.field().ID():
                return FieldAccess(left, ctx.field().ID().getText())
            return FieldAccess(left, str(right))
        elif ctx.callfuncdecl() and ctx.access_field():
            funName, args = self.visit(ctx.callfuncdecl())
            left = self.visit(ctx.access_field())
            return MethCall(left, funName, args)
        elif ctx.callfuncdecl():
            funName, args = self.visit(ctx.callfuncdecl())
            return FuncCall(funName, args)
        return self.visit(ctx.field())
    
    def visitField(self, ctx:MiniGoParser.FieldContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.array_access_field():
            return self.visit(ctx.array_access_field())
        elif ctx.expression_int():
            return self.visit(ctx.expression_int())
        elif ctx.expression_float():
            return self.visit(ctx.expression_float())
        elif ctx.expression_string():
            return self.visit(ctx.expression_string())
        elif ctx.expression_boolean():
            return self.visit(ctx.expression_boolean())
    
    # array type    
    def visitArrays_type(self, ctx:MiniGoParser.Arrays_typeContext):
        dimens = [self.visit(size) for size in ctx.array_size()]
        eleType = None
        if ctx.PRIMITIVE_TYPE():
            eleType = getPrimitiveType(ctx.PRIMITIVE_TYPE().getText())
        elif ctx.ID():
            eleType = Id(ctx.ID().getText())
        return dimens, eleType
    
    # array decl
    def visitExpression_array(self, ctx:MiniGoParser.Expression_arrayContext):
        dimens, eleType = self.visit(ctx.arrays_type())
        array_value = self.visit(ctx.array_instance())
        return ArrayLiteral(dimens, eleType, array_value)
    
    def visitArray_instance(self, ctx:MiniGoParser.Array_instanceContext):
        return [self.visit(i) for i in ctx.array_value()]
    
    def visitArray_value(self, ctx:MiniGoParser.Array_valueContext):
        if ctx.expression_int():
            return self.visit(ctx.expression_int())
        elif ctx.expression_float():
            return self.visit(ctx.expression_float())
        elif ctx.expression_string():
            return self.visit(ctx.expression_string())
        elif ctx.expression_boolean():
            return self.visit(ctx.expression_boolean())
        elif ctx.struct_value():
            name, elements = self.visit(ctx.struct_value())
            return StructLiteral(name, elements)
        elif ctx.array_value():
            return [self.visit(i) for i in ctx.array_value()]
        return []

    # value
    def visitValue_assign(self, ctx:MiniGoParser.Value_assignContext): 
        if ctx.expression_boolean():
            return self.visit(ctx.expression_boolean())       
        elif ctx.expression_int():
            return self.visit(ctx.expression_int())
        elif ctx.expression_float():
            return self.visit(ctx.expression_float())
        elif ctx.expression_string():
            return self.visit(ctx.expression_string())
        elif ctx.expression_array():
            return self.visit(ctx.expression_array())
        elif ctx.struct_value():
            name, elements = self.visit(ctx.struct_value())
            return StructLiteral(name, elements)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.value_assign():
            return self.visit(ctx.value_assign())
    
    # struct value    
    def visitStruct_value(self, ctx:MiniGoParser.Struct_valueContext):
        name = ctx.ID().getText()
        elements = self.visit(ctx.field_value()) if ctx.field_value() else []
        return name, elements
    
    def visitField_value(self, ctx:MiniGoParser.Field_valueContext):
        lst_id = ctx.ID()
        lst_value_assign = ctx.value_assign()
        elements = []
        
        for j in range(len(lst_id)):
            field_name = lst_id[j].getText()
            field_value = self.visit(lst_value_assign[j]) if j < len(lst_value_assign) else None
            elements.append((field_name, field_value))

        return elements
    
    # call func decl
    def visitCallfuncdecl(self, ctx:MiniGoParser.CallfuncdeclContext):
        funName = ctx.ID().getText()
        args = self.visit(ctx.argu_list()) if ctx.argu_list() else []
        return funName, args
    
    def visitArgu_list(self, ctx:MiniGoParser.Argu_listContext):
        return [self.visit(ctx.value_assign()[j]) for j in range(len(ctx.value_assign()))]
    
    # struct decl
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        name = ctx.ID().getText()
        elements = [self.visit(i) for i in ctx.struct_field()]
        return StructType(name, elements, [])
    
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        name = ctx.ID().getText()
        fieldType = self.visit(ctx.struct_fieldType())
        return (name, fieldType)
    
    def visitStruct_fieldType(self, ctx:MiniGoParser.Struct_fieldTypeContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.PRIMITIVE_TYPE():
            return getPrimitiveType(ctx.PRIMITIVE_TYPE().getText())
        elif ctx.arrays_type():
            dimens, eleType = self.visit(ctx.arrays_type())
            return ArrayType(dimens, eleType)
    
    # interface decl
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        name = ctx.ID().getText()
        methods = [self.visit(meth) for meth in ctx.interface_field()]
        return InterfaceType(name, methods)
    
    def visitInterface_field(self, ctx:MiniGoParser.Interface_fieldContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.interfaceParams()) if ctx.interfaceParams() else []
        retType = self.visit(ctx.interfaceType()) if ctx.interfaceType() else VoidType()
        return Prototype(name, params, retType)
    
    def visitInterfaceParams(self, ctx:MiniGoParser.InterfaceParamsContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.interfaceParam()) + self.visit(ctx.interfaceParams())
        return self.visit(ctx.interfaceParam())
    
    def visitInterfaceParam(self, ctx:MiniGoParser.InterfaceParamContext):
        return [self.visit(ctx.interfaceType())]
    
    def visitInterfaceListName(self, ctx:MiniGoParser.InterfaceListNameContext):
        if ctx.getChildCount() == 3:
            return [ctx.ID().getText()] + self.visit(ctx.interfaceListName())
        return [ctx.ID().getText()]
    
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        if ctx.PRIMITIVE_TYPE():
            return getPrimitiveType(ctx.PRIMITIVE_TYPE().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arrays_type():
            dimens, eleType = self.visit(ctx.arrays_type())
            return ArrayType(dimens, eleType)
    
    # break decl
    def visitBreakdecl(self, ctx:MiniGoParser.BreakdeclContext):
        return Break()
    
    # continue decl
    def visitContinuedecl(self, ctx:MiniGoParser.ContinuedeclContext):
        return Continue()
    
    # return decl
    def visitReturndecl(self, ctx:MiniGoParser.ReturndeclContext):
        return Return(self.visit(ctx.value_assign()) if ctx.value_assign() else None)
    
    # array size
    def visitArray_size(self, ctx:MiniGoParser.Array_sizeContext):
        return self.visit(ctx.expression_int())
    
    # expression int
    def visitExpression_int(self, ctx:MiniGoParser.Expression_intContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expression_int())
            right = self.visit(ctx.add_int())
            return BinaryOp(op, left, right)
        elif ctx.add_int():
            return self.visit(ctx.add_int())
    
    def visitAdd_int(self, ctx: MiniGoParser.Add_intContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.add_int())
            right = self.visit(ctx.mul_int())
            return BinaryOp(op, left, right)
        elif ctx.mul_int():
            return self.visit(ctx.mul_int())

    def visitMul_int(self, ctx: MiniGoParser.Mul_intContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.mul_int())
            right = self.visit(ctx.unary_int())
            return BinaryOp(op, left, right)
        elif ctx.unary_int():
            return self.visit(ctx.unary_int())
        
    def visitUnary_int(self, ctx:MiniGoParser.Unary_intContext):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            expr = self.visit(ctx.unary_int())
            return UnaryOp(op, expr)
        elif ctx.term_int():
            return self.visit(ctx.term_int())
                
    def visitTerm_int(self, ctx:MiniGoParser.Term_intContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INT_LITERALS():
            return getIntLiteral(ctx)
        elif ctx.access_field():
            return self.visit(ctx.access_field())
        elif ctx.expression_array():
            return self.visit(ctx.expression_array())
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expression_int())
        
    # expression float
    def visitExpression_float(self, ctx:MiniGoParser.Expression_floatContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expression_float())
            right = self.visit(ctx.add_float())
            return BinaryOp(op, left, right)
        elif ctx.add_float():
            return self.visit(ctx.add_float())

    def visitAdd_float(self, ctx: MiniGoParser.Add_floatContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.add_float())
            right = self.visit(ctx.mul_float())
            return BinaryOp(op, left, right)
        elif ctx.mul_float():
            return self.visit(ctx.mul_float())

    def visitMul_float(self, ctx: MiniGoParser.Mul_floatContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.mul_float())
            right = self.visit(ctx.unary_float())
            return BinaryOp(op, left, right)
        elif ctx.unary_float():
            return self.visit(ctx.unary_float())
        
    def visitUnary_float(self, ctx:MiniGoParser.Unary_floatContext):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            expr = self.visit(ctx.unary_float())
            return UnaryOp(op, expr)
        elif ctx.term_float():
            return self.visit(ctx.term_float())
    
    def visitTerm_float(self, ctx:MiniGoParser.Term_floatContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INT_LITERALS():
            return getIntLiteral(ctx)
        elif ctx.FLOAT_LITERALS():
            return getFloatLiteral(ctx)
        elif ctx.access_field():
            return self.visit(ctx.access_field())
        elif ctx.expression_array():
            return self.visit(ctx.expression_array())
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expression_float())
      
    # expression string  
    def visitExpression_string(self, ctx:MiniGoParser.Expression_stringContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expression_string())
            right = self.visit(ctx.plus_string())
            return BinaryOp(op, left, right)
        elif ctx.plus_string():
            return self.visit(ctx.plus_string())

    def visitPlus_string(self, ctx:MiniGoParser.Plus_stringContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.plus_string())
            right = self.visit(ctx.term_plus())
            return BinaryOp(op, left, right)
        elif ctx.term_plus():
            return self.visit(ctx.term_plus())
    
    def visitTerm_plus(self, ctx:MiniGoParser.Term_plusContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.STRING_LITERALS():
            return getStringLiteral(ctx)
        elif ctx.access_field():
            return self.visit(ctx.access_field())
        elif ctx.expression_array():
            return self.visit(ctx.expression_array())
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expression_string())

    # expression boolean
    def visitExpression_boolean(self, ctx:MiniGoParser.Expression_booleanContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expression_boolean())
            right = self.visit(ctx.and_boolean())
            return BinaryOp(op, left, right)
        elif ctx.and_boolean():
            return self.visit(ctx.and_boolean())
    
    def visitAnd_boolean(self, ctx:MiniGoParser.And_booleanContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.and_boolean())
            right = self.visit(ctx.compare_boolean())
            return BinaryOp(op, left, right)
        elif ctx.compare_boolean():
            return self.visit(ctx.compare_boolean())    
    
    def visitCompare_boolean(self, ctx:MiniGoParser.Compare_booleanContext):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.compare_boolean())
            right = self.visit(ctx.unary_boolean())
            return BinaryOp(op, left, right)
        elif ctx.unary_boolean():
            return self.visit(ctx.unary_boolean())
        
    def visitUnary_boolean(self, ctx:MiniGoParser.Unary_booleanContext):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            expr = self.visit(ctx.unary_boolean())
            return UnaryOp(op, expr)
        elif ctx.term_boolean():
            return self.visit(ctx.term_boolean())
    
    def visitTerm_boolean(self, ctx:MiniGoParser.Term_booleanContext):
        if ctx.BOOLEAN_LITERALS():
            return getBooleanLiteral(ctx)
        elif ctx.expression_int():
            return self.visit(ctx.expression_int())
        elif ctx.expression_float():
            return self.visit(ctx.expression_float())
        elif ctx.expression_string():
            return self.visit(ctx.expression_string())
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.expression_boolean())
    
    # array access
    def visitArray_access_field(self, ctx:MiniGoParser.Array_access_fieldContext):
        arr = self.visit(ctx.arr_name())
        idx = [self.visit(i) for i in ctx.array_idx()]
        return ArrayCell(arr, idx)
    
    def visitArr_name(self, ctx:MiniGoParser.Arr_nameContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.callfuncdecl():
            funName, args = self.visit(ctx.callfuncdecl())
            return FuncCall(funName, args)
        elif ctx.INT_LITERALS():
            return getIntLiteral(ctx)
        elif ctx.FLOAT_LITERALS():
            return getFloatLiteral(ctx)
        elif ctx.STRING_LITERALS():
            return getStringLiteral(ctx)
        elif ctx.BOOLEAN_LITERALS(ctx):
            return getBooleanLiteral(ctx)
        elif ctx.expression_int():
            return self.visit(ctx.expression_int())
        elif ctx.expression_float():
            return self.visit(ctx.expression_float())
        elif ctx.expression_string():
            return self.visit(ctx.expression_string())
        elif ctx.expression_boolean():
            return self.visit(ctx.expression_boolean())
    
    def visitArray_idx(self, ctx:MiniGoParser.Array_idxContext):
        if ctx.expression_int():
            return self.visit(ctx.expression_int())
        elif ctx.expression_float():
            return self.visit(ctx.expression_float())
        elif ctx.expression_string():
            return self.visit(ctx.expression_string())
        elif ctx.expression_boolean():
            return self.visit(ctx.expression_boolean())