# pylint: disable=invalid-name
from antlr4 import TerminalNode
from antlr4.error.ErrorListener import ErrorListener

from math_expression.MathExpressionListener import MathExpressionListener
from math_expression.MathExpressionParser import MathExpressionParser


class IdentifiersListener(MathExpressionListener):
    """
    Parser listener that saves the names of identifiers found in the expression. It can change its
    value in the parsed text from identifier to dataframe["identifier"] if dataframe_name is not None.
    """

    def __init__(self, df_name: str | None = None):
        super().__init__()
        self._df_name = df_name
        self._identifiers: list[str] = []

    def exitValue(self, ctx: MathExpressionParser.ValueContext) -> None:
        """Append identifier name to list. It can change its value in the parsed text from identifier
        to dataframe["identifier"] if dataframe_name is not None.

        :param ctx: parser context
        """
        for child in ctx.getChildren():
            if isinstance(child, TerminalNode) and child.symbol.type == MathExpressionParser.Identifier:  # type: ignore
                self._identifiers.append(child.symbol.text)  # type: ignore
                if self._df_name is not None:
                    child.symbol.text = self._df_name + '["' + child.symbol.text + '"]'  # type: ignore

    def getIdentifiers(self) -> list[str]:
        """Returns list of identifiers found in parsed expression.

        :return: list of identifiers found in parsed expression
        """
        return self._identifiers


class LexerErrorListener(ErrorListener):
    """Lexer ErrorListener that counts the number of errors found."""

    def __init__(self) -> None:
        super().__init__()
        self._errors = 0

    def syntaxError(  # type: ignore # pylint: disable=too-many-arguments,too-many-positional-arguments
        self, recognizer, offendingSymbol, line, column, msg, e
    ) -> None:
        """Increment number of error found in analysed text."""
        self._errors += 1

    def getNumberOfSyntaxErrors(self) -> int:
        """Return number of syntex errors found in analysed text.

        :return: Number of syntex errors found in analysed text.
        """
        return self._errors
