# Generated from MathExpression.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MathExpressionParser import MathExpressionParser
else:
    from MathExpressionParser import MathExpressionParser

# This class defines a complete listener for a parse tree produced by MathExpressionParser.
class MathExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by MathExpressionParser#expression.
    def enterExpression(self, ctx:MathExpressionParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MathExpressionParser#expression.
    def exitExpression(self, ctx:MathExpressionParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MathExpressionParser#math_expression.
    def enterMath_expression(self, ctx:MathExpressionParser.Math_expressionContext):
        pass

    # Exit a parse tree produced by MathExpressionParser#math_expression.
    def exitMath_expression(self, ctx:MathExpressionParser.Math_expressionContext):
        pass


    # Enter a parse tree produced by MathExpressionParser#maybe_multiply_expression.
    def enterMaybe_multiply_expression(self, ctx:MathExpressionParser.Maybe_multiply_expressionContext):
        pass

    # Exit a parse tree produced by MathExpressionParser#maybe_multiply_expression.
    def exitMaybe_multiply_expression(self, ctx:MathExpressionParser.Maybe_multiply_expressionContext):
        pass


    # Enter a parse tree produced by MathExpressionParser#maybe_negative_value.
    def enterMaybe_negative_value(self, ctx:MathExpressionParser.Maybe_negative_valueContext):
        pass

    # Exit a parse tree produced by MathExpressionParser#maybe_negative_value.
    def exitMaybe_negative_value(self, ctx:MathExpressionParser.Maybe_negative_valueContext):
        pass


    # Enter a parse tree produced by MathExpressionParser#value.
    def enterValue(self, ctx:MathExpressionParser.ValueContext):
        pass

    # Exit a parse tree produced by MathExpressionParser#value.
    def exitValue(self, ctx:MathExpressionParser.ValueContext):
        pass



del MathExpressionParser