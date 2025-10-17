# Generated from MathExpression.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,1,2,1,2,5,2,25,8,2,10,
        2,12,2,28,9,2,1,3,3,3,31,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        41,8,4,1,4,0,0,5,0,2,4,6,8,0,1,1,0,1,2,42,0,10,1,0,0,0,2,13,1,0,
        0,0,4,21,1,0,0,0,6,30,1,0,0,0,8,40,1,0,0,0,10,11,3,2,1,0,11,12,5,
        0,0,1,12,1,1,0,0,0,13,18,3,4,2,0,14,15,7,0,0,0,15,17,3,4,2,0,16,
        14,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,
        0,20,18,1,0,0,0,21,26,3,6,3,0,22,23,5,3,0,0,23,25,3,6,3,0,24,22,
        1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,5,1,0,0,0,28,
        26,1,0,0,0,29,31,5,2,0,0,30,29,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,
        0,32,33,3,8,4,0,33,7,1,0,0,0,34,41,5,6,0,0,35,41,5,9,0,0,36,37,5,
        4,0,0,37,38,3,2,1,0,38,39,5,5,0,0,39,41,1,0,0,0,40,34,1,0,0,0,40,
        35,1,0,0,0,40,36,1,0,0,0,41,9,1,0,0,0,4,18,26,30,40
    ]

class MathExpressionParser ( Parser ):

    grammarFileName = "MathExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Literal", "Int", "Float", 
                      "Identifier", "Whitespace" ]

    RULE_expression = 0
    RULE_math_expression = 1
    RULE_maybe_multiply_expression = 2
    RULE_maybe_negative_value = 3
    RULE_value = 4

    ruleNames =  [ "expression", "math_expression", "maybe_multiply_expression", 
                   "maybe_negative_value", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    Literal=6
    Int=7
    Float=8
    Identifier=9
    Whitespace=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def math_expression(self):
            return self.getTypedRuleContext(MathExpressionParser.Math_expressionContext,0)


        def EOF(self):
            return self.getToken(MathExpressionParser.EOF, 0)

        def getRuleIndex(self):
            return MathExpressionParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = MathExpressionParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.math_expression()
            self.state = 11
            self.match(MathExpressionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Math_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def maybe_multiply_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExpressionParser.Maybe_multiply_expressionContext)
            else:
                return self.getTypedRuleContext(MathExpressionParser.Maybe_multiply_expressionContext,i)


        def getRuleIndex(self):
            return MathExpressionParser.RULE_math_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_expression" ):
                listener.enterMath_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_expression" ):
                listener.exitMath_expression(self)




    def math_expression(self):

        localctx = MathExpressionParser.Math_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_math_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.maybe_multiply_expression()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 14
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 15
                self.maybe_multiply_expression()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Maybe_multiply_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def maybe_negative_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExpressionParser.Maybe_negative_valueContext)
            else:
                return self.getTypedRuleContext(MathExpressionParser.Maybe_negative_valueContext,i)


        def getRuleIndex(self):
            return MathExpressionParser.RULE_maybe_multiply_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaybe_multiply_expression" ):
                listener.enterMaybe_multiply_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaybe_multiply_expression" ):
                listener.exitMaybe_multiply_expression(self)




    def maybe_multiply_expression(self):

        localctx = MathExpressionParser.Maybe_multiply_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_maybe_multiply_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.maybe_negative_value()
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 22
                self.match(MathExpressionParser.T__2)
                self.state = 23
                self.maybe_negative_value()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Maybe_negative_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(MathExpressionParser.ValueContext,0)


        def getRuleIndex(self):
            return MathExpressionParser.RULE_maybe_negative_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaybe_negative_value" ):
                listener.enterMaybe_negative_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaybe_negative_value" ):
                listener.exitMaybe_negative_value(self)




    def maybe_negative_value(self):

        localctx = MathExpressionParser.Maybe_negative_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_maybe_negative_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 29
                self.match(MathExpressionParser.T__1)


            self.state = 32
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Literal(self):
            return self.getToken(MathExpressionParser.Literal, 0)

        def Identifier(self):
            return self.getToken(MathExpressionParser.Identifier, 0)

        def math_expression(self):
            return self.getTypedRuleContext(MathExpressionParser.Math_expressionContext,0)


        def getRuleIndex(self):
            return MathExpressionParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = MathExpressionParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 34
                self.match(MathExpressionParser.Literal)
                pass
            elif token in [9]:
                self.state = 35
                self.match(MathExpressionParser.Identifier)
                pass
            elif token in [4]:
                self.state = 36
                self.match(MathExpressionParser.T__3)
                self.state = 37
                self.math_expression()
                self.state = 38
                self.match(MathExpressionParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





