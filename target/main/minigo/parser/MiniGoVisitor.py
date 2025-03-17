# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#expression_string.
    def visitExpression_string(self, ctx:MiniGoParser.Expression_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#plus_string.
    def visitPlus_string(self, ctx:MiniGoParser.Plus_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_plus.
    def visitTerm_plus(self, ctx:MiniGoParser.Term_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_float.
    def visitExpression_float(self, ctx:MiniGoParser.Expression_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#add_float.
    def visitAdd_float(self, ctx:MiniGoParser.Add_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mul_float.
    def visitMul_float(self, ctx:MiniGoParser.Mul_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary_float.
    def visitUnary_float(self, ctx:MiniGoParser.Unary_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_float.
    def visitTerm_float(self, ctx:MiniGoParser.Term_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_int.
    def visitExpression_int(self, ctx:MiniGoParser.Expression_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#add_int.
    def visitAdd_int(self, ctx:MiniGoParser.Add_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mul_int.
    def visitMul_int(self, ctx:MiniGoParser.Mul_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary_int.
    def visitUnary_int(self, ctx:MiniGoParser.Unary_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_int.
    def visitTerm_int(self, ctx:MiniGoParser.Term_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_boolean.
    def visitExpression_boolean(self, ctx:MiniGoParser.Expression_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#and_boolean.
    def visitAnd_boolean(self, ctx:MiniGoParser.And_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compare_boolean.
    def visitCompare_boolean(self, ctx:MiniGoParser.Compare_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary_boolean.
    def visitUnary_boolean(self, ctx:MiniGoParser.Unary_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_boolean.
    def visitTerm_boolean(self, ctx:MiniGoParser.Term_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_array.
    def visitExpression_array(self, ctx:MiniGoParser.Expression_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_size.
    def visitArray_size(self, ctx:MiniGoParser.Array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrays_type.
    def visitArrays_type(self, ctx:MiniGoParser.Arrays_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_instance.
    def visitArray_instance(self, ctx:MiniGoParser.Array_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_value.
    def visitArray_value(self, ctx:MiniGoParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_idx.
    def visitArray_idx(self, ctx:MiniGoParser.Array_idxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_access_field.
    def visitArray_access_field(self, ctx:MiniGoParser.Array_access_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_name.
    def visitArr_name(self, ctx:MiniGoParser.Arr_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access_field.
    def visitAccess_field(self, ctx:MiniGoParser.Access_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_value.
    def visitStruct_value(self, ctx:MiniGoParser.Struct_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_value.
    def visitField_value(self, ctx:MiniGoParser.Field_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relational.
    def visitRelational(self, ctx:MiniGoParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#other_operations.
    def visitOther_operations(self, ctx:MiniGoParser.Other_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcParams.
    def visitFuncParams(self, ctx:MiniGoParser.FuncParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcParam.
    def visitFuncParam(self, ctx:MiniGoParser.FuncParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcListName.
    def visitFuncListName(self, ctx:MiniGoParser.FuncListNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcType.
    def visitFuncType(self, ctx:MiniGoParser.FuncTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_fieldType.
    def visitStruct_fieldType(self, ctx:MiniGoParser.Struct_fieldTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacedecl.
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_field.
    def visitInterface_field(self, ctx:MiniGoParser.Interface_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceParams.
    def visitInterfaceParams(self, ctx:MiniGoParser.InterfaceParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceParam.
    def visitInterfaceParam(self, ctx:MiniGoParser.InterfaceParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceListName.
    def visitInterfaceListName(self, ctx:MiniGoParser.InterfaceListNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceType.
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varType.
    def visitVarType(self, ctx:MiniGoParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#shortvardecl.
    def visitShortvardecl(self, ctx:MiniGoParser.ShortvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_operators.
    def visitAssign_operators(self, ctx:MiniGoParser.Assign_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returndecl.
    def visitReturndecl(self, ctx:MiniGoParser.ReturndeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callfuncdecl.
    def visitCallfuncdecl(self, ctx:MiniGoParser.CallfuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argu_list.
    def visitArgu_list(self, ctx:MiniGoParser.Argu_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#value_assign.
    def visitValue_assign(self, ctx:MiniGoParser.Value_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakdecl.
    def visitBreakdecl(self, ctx:MiniGoParser.BreakdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continuedecl.
    def visitContinuedecl(self, ctx:MiniGoParser.ContinuedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifelsedecl.
    def visitIfelsedecl(self, ctx:MiniGoParser.IfelsedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elifdecls.
    def visitElifdecls(self, ctx:MiniGoParser.ElifdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elifdecl.
    def visitElifdecl(self, ctx:MiniGoParser.ElifdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elsedecl.
    def visitElsedecl(self, ctx:MiniGoParser.ElsedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifelsedecl_inside_loop.
    def visitIfelsedecl_inside_loop(self, ctx:MiniGoParser.Ifelsedecl_inside_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elifdecls_inside_loop.
    def visitElifdecls_inside_loop(self, ctx:MiniGoParser.Elifdecls_inside_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elifdecl_inside_loop.
    def visitElifdecl_inside_loop(self, ctx:MiniGoParser.Elifdecl_inside_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elsedecl_inside_loop.
    def visitElsedecl_inside_loop(self, ctx:MiniGoParser.Elsedecl_inside_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forloopdecl.
    def visitForloopdecl(self, ctx:MiniGoParser.ForloopdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_access_value.
    def visitFor_access_value(self, ctx:MiniGoParser.For_access_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_arr.
    def visitFor_arr(self, ctx:MiniGoParser.For_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_inside_loop.
    def visitBlock_inside_loop(self, ctx:MiniGoParser.Block_inside_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initialization.
    def visitInitialization(self, ctx:MiniGoParser.InitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update.
    def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
        return self.visitChildren(ctx)



del MiniGoParser