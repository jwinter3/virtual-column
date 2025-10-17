import pandas as pd
from antlr4 import CommonTokenStream, InputStream
from pandas.api.types import is_numeric_dtype

from listeners import IdentifiersListener, LexerErrorListener
from math_expression.MathExpressionLexer import MathExpressionLexer
from math_expression.MathExpressionParser import MathExpressionParser


def _is_column_name_correct(name: str) -> bool:
    return all(char.isalpha() or char == "_" for char in name)


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """Returns new pandas DataFrame that include original data along with an additional column calculated
       based on specified operation.

    :param df: Any pandas DataFrame. Column labels must consist only of letters and underscores (_).
    :param role: A mathematical expression defining how to compute the value for the virtual column.
                 For example, first_column - second_colum
                 Support basic operations: addition (+), subtraction (-), and multiplication (*)
                 and expression in parentheses.
    :param new_column: The name of the new virtual column to be added.
                       Label must consist only of letters and underscores (_).
    :return: New pandas DataFrame that include original data along with an additional column calculated
             based on specified operation or empty pandas DataFrame if the role or any label is incorrect.
    """
    if not _is_column_name_correct(new_column):
        return pd.DataFrame([])

    if not all(_is_column_name_correct(column) for column in df.columns):
        return pd.DataFrame([])

    lexer = MathExpressionLexer(InputStream(role))
    lexer_listener = LexerErrorListener()
    lexer.addErrorListener(lexer_listener)

    parser = MathExpressionParser(CommonTokenStream(lexer))
    parser_listener = IdentifiersListener(df_name="df")
    parser.addParseListener(parser_listener)
    tree = parser.expression()  # type: ignore

    if lexer_listener.getNumberOfSyntaxErrors() > 0 or parser.getNumberOfSyntaxErrors() > 0:  # type: ignore
        return pd.DataFrame([])

    if any(identifier not in df.columns for identifier in parser_listener.getIdentifiers()):
        return pd.DataFrame([])

    if any(not is_numeric_dtype(df[identifier]) for identifier in parser_listener.getIdentifiers()):
        return pd.DataFrame([])

    return df.assign(**{new_column: pd.eval(tree.getText().removesuffix("<EOF>"))})  # type: ignore
