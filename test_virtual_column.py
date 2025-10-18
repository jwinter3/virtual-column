# pylint: disable=missing-function-docstring
import pandas as pd

from solution import add_virtual_column


def test_sum_of_two_columns() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one+label_two", "label_three")
    assert df_result.equals(df_expected), (
        "The function should sum the columns: label_one and label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_multiplication_of_two_columns() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 1]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one * label_two", "label_three")
    assert df_result.equals(df_expected), (
        "The function should multiply the columns: label_one and label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_subtraction_of_two_columns() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 0]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one - label_two", "label_three")
    assert df_result.equals(df_expected), (
        "The function should subtract the columns: label_one and label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_empty_result_when_invalid_labels() -> None:
    df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one + label_two", "label3")
    assert df_result.empty, (
        'Should return an empty df when the "new_column" is invalid.\n\n'
        + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )


def test_empty_result_when_invalid_roles() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_result = add_virtual_column(df, "label&one + label_two", "label_three")
    assert df_result.empty, (
        "Should return an empty df when the role have invalid character: '&'.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, "label_five + label_two", "label_three")
    assert df_result.empty, (
        "Should return an empty df when the role have a column which isn't in the df: 'label_five'.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )


def test_when_extra_spaces_in_roles() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one + label_two ", "label_three")
    assert df_result.equals(df_expected), (
        "Should work when the role have spaces between the operation and the column.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )
    df_result = add_virtual_column(df, "  label_one + label_two ", "label_three")
    assert df_result.equals(df_expected), (
        "Should work when the role have extra spaces in the start/end.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_of_two_columns_more_complex_data() -> None:
    df = pd.DataFrame([[1, 2], [2, 3], [3, 4]], columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 3], [2, 3, 5], [3, 4, 7]], columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one+label_two", "label_three")
    assert df_result.equals(df_expected), (
        "The function should sum the columns: label_one and label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_copy_of_one_column() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 1]] * 2, columns=["label_one", "label_two", "label_one_copy"])
    df_result = add_virtual_column(df, "label_one", "label_one_copy")
    assert df_result.equals(df_expected), (
        "The function should copy of the column: label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_negation_of_one_column() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, -1]] * 2, columns=["label_one", "label_two", "minus_label_one"])
    df_result = add_virtual_column(df, "-label_one", "minus_label_one")
    assert df_result.equals(df_expected), (
        "The function should negation of the column: label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_of_three_columns() -> None:
    df = pd.DataFrame([[1, 1, 2]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 1, 2, 4]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "label_one+label_two+label_three", "label_four")
    assert df_result.equals(df_expected), (
        "The function should sum the columns: label_one, label_two and label_three.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_new_column_with_int() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 1]] * 2, columns=["label_one", "label_two", "one"])
    df_result = add_virtual_column(df, "1", "one")
    assert df_result.equals(df_expected), (
        "The function should add column with const value: 1.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_new_column_with_zero() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 0]] * 2, columns=["label_one", "label_two", "zero"])
    df_result = add_virtual_column(df, "0", "zero")
    assert df_result.equals(df_expected), (
        "The function should add column with const value: 0.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_new_column_with_float() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 1.01]] * 2, columns=["label_one", "label_two", "float"])
    df_result = add_virtual_column(df, "1.01", "float")
    assert df_result.equals(df_expected), (
        "The function should add column with const value: 1.01.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_new_column_with_fraction() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 0.1]] * 2, columns=["label_one", "label_two", "fraction"])
    df_result = add_virtual_column(df, "0.1", "fraction")
    assert df_result.equals(df_expected), (
        "The function should add column with const value: 0.1.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_new_column_with_negative_int() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, -1]] * 2, columns=["label_one", "label_two", "minus_one"])
    df_result = add_virtual_column(df, "-1", "minus_one")
    assert df_result.equals(df_expected), (
        "The function should add column with const value: -1.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_new_column_with_negative_zero() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 0]] * 2, columns=["label_one", "label_two", "zero"])
    df_result = add_virtual_column(df, "-0", "zero")
    assert df_result.equals(df_expected), (
        "The function should add column with const value: 0.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_new_column_with_negative_float() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, -1.01]] * 2, columns=["label_one", "label_two", "minus_float"])
    df_result = add_virtual_column(df, "-1.01", "minus_float")
    assert df_result.equals(df_expected), (
        "The function should add column with const value: 1.01.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_new_column_with_negative_fraction() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, -0.1]] * 2, columns=["label_one", "label_two", "minus_fraction"])
    df_result = add_virtual_column(df, "-0.1", "minus_fraction")
    assert df_result.equals(df_expected), (
        "The function should add column with const value: 0.1.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_of_one_column_and_int() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 5]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one+4", "label_three")
    assert df_result.equals(df_expected), (
        "The function should sum the one column and int: label_one and 4.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_of_int_and_one_column() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 5]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "4+label_one", "label_three")
    assert df_result.equals(df_expected), (
        "The function should sum the int and one column: 4 and label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_of_one_column_and_float() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 5.5]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one+4.5", "label_three")
    assert df_result.equals(df_expected), (
        "The function should sum the one column and float: label_one and 4.5.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_of_float_and_one_column() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 5.5]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "4.5+label_one", "label_three")
    assert df_result.equals(df_expected), (
        "The function should sum the float and one column: 4.5 and label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_subtraction_of_one_column_and_int() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, -3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one-4", "label_three")
    assert df_result.equals(df_expected), (
        "The function should subtract the one column and int: label_one and 4.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_subtraction_of_int_and_one_column() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "4-label_one", "label_three")
    assert df_result.equals(df_expected), (
        "The function should subtract the int and one column: 4 and label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_subtraction_of_one_column_and_float() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, -3.5]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one-4.5", "label_three")
    assert df_result.equals(df_expected), (
        "The function should subtract the one column and float: label_one and 4.5.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_subtraction_of_float_and_one_column() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 3.5]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "4.5-label_one", "label_three")
    assert df_result.equals(df_expected), (
        "The function should subtract the float and one column: 4.5 and label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_multiplication_of_one_column_and_int() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 4]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one*4", "label_three")
    assert df_result.equals(df_expected), (
        "The function should multiply the one column and int: label_one and 4.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_multiplication_of_int_and_one_column() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 4]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "4*label_one", "label_three")
    assert df_result.equals(df_expected), (
        "The function should multiply the int and one column: 4 and label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_multiplication_of_one_column_and_float() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 4.5]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one*4.5", "label_three")
    assert df_result.equals(df_expected), (
        "The function should multiply the one column and float: label_one and 4.5.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_multiplication_of_float_and_one_column() -> None:
    df = pd.DataFrame([[1, 2]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 2, 4.5]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "4.5*label_one", "label_three")
    assert df_result.equals(df_expected), (
        "The function should multiply the float and one column: 4.5 and label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_subtraction_of_three_columns() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 0]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "label_three - label_two - label_one", "label_four")
    assert df_result.equals(df_expected), (
        "The function should subtract the columns: label_three - label_two - label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_and_subtraction_three_columns() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 2]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "label_three - label_two + label_one", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: label_three - label_two + label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_multiplication_of_three_columns() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 6]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "label_three * label_two * label_one", "label_four")
    assert df_result.equals(df_expected), (
        "The function should multiply the columns: label_three, label_two and label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_of_two_ints() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2+1", "label_three")
    assert df_result.equals(df_expected), (
        "The function should sum the ints: 2 and 1.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_multiplication_of_two_ints() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2*1", "label_three")
    assert df_result.equals(df_expected), (
        "The function should multiply the ints: 2 and 1.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_subtraction_of_two_ints() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 1]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2-1", "label_three")
    assert df_result.equals(df_expected), (
        "The function should subtract the ints: 2 and 1.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_of_two_floats() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 3.75]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2.5+1.25", "label_three")
    assert df_result.equals(df_expected), (
        "The function should sum the floats: 2.5 and 1.25.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_multiplication_of_two_floats() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 3.125]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2.5*1.25", "label_three")
    assert df_result.equals(df_expected), (
        "The function should multiply the floats: 2.5 and 1.25.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_subtraction_of_two_floats() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 1.25]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2.5-1.25", "label_three")
    assert df_result.equals(df_expected), (
        "The function should subtract the floats: 2.5 and 1.25.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_of_int_and_float() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 3.25]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2+1.25", "label_three")
    assert df_result.equals(df_expected), (
        "The function should sum the numbers: 2 and 1.25.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_multiplication_of_int_and_float() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2.5]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2*1.25", "label_three")
    assert df_result.equals(df_expected), (
        "The function should multiply the numbers: 2 and 1.25.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_subtraction_of_int_and_float() -> None:
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 0.75]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2-1.25", "label_three")
    assert df_result.equals(df_expected), (
        "The function should subtract the numbers: 2 and 1.25.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_and_multiplication_three_columns_1() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 5]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "label_three + label_two * label_one", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: label_three + label_two * label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_and_multiplication_three_columns_2() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 7]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "label_three * label_two + label_one", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: label_three * label_two + label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_substraction_and_multiplication_three_columns_1() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 1]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "label_three - label_two * label_one", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: label_three - label_two * label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_substraction_and_multiplication_three_columns_2() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 5]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "label_three * label_two - label_one", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: label_three * label_two - label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_substraction_and_multiplication_columns_and_consts_1() -> None:
    df = pd.DataFrame([[1.0, 2.0, 3.0]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame(
        [[1.0, 2.0, 3.0, 7.0]] * 2, columns=["label_one", "label_two", "label_three", "label_four"]
    )
    df_result = add_virtual_column(df, "3*label_three - label_two", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*label_three - label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_substraction_and_multiplication_columns_and_consts_2() -> None:
    df = pd.DataFrame([[1.0, 2.0, 3.0]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame(
        [[1.0, 2.0, 3.0, 3.5]] * 2, columns=["label_one", "label_two", "label_three", "label_four"]
    )
    df_result = add_virtual_column(df, "label_three - 0.25*label_two + label_one", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: label_three - 0.25*label_two + label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_sum_three_times_one_column() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 9]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "label_three  + label_three+label_three", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: label_three  + label_three+label_three.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_expression_with_parenthesis() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 7.0]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "2*(label_three - 0.25*label_two + label_one)", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 2*(label_three - 0.25*label_two + label_one.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_expression_with_nested_parenthesis() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_expected = pd.DataFrame([[1, 2, 3, 4.5]] * 2, columns=["label_one", "label_two", "label_three", "label_four"])
    df_result = add_virtual_column(df, "2*(label_three - 0.25*(label_two + label_one)-0.25)+0.5", "label_four")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression:"
        + "2*(label_three - 0.25*(label_two + label_one)-0.25)+0.5.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_empty_result_when_operator_at_end_of_role() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "2*label_three+", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )


def test_empty_result_when_operator_at_start_of_role() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "*2*label_three", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )


def test_empty_result_when_column_name_in_df_is_invalid() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label3"])
    df_result = add_virtual_column(df, "2*label_three", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the column name in dataframe is invalid.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )


def test_empty_result_when_invalid_operator() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_three/2", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )


def test_empty_result_when_space_in_column_label() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_ three * 2", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )


def test_empty_result_when_invalid_expression() -> None:
    df = pd.DataFrame([[1, 2, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_three(label_two)", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, "label_three+()", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, "x+y", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, "001+2", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, ".1+2", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, "1+2.", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, "..1+2", "label_four")
    assert df_result.empty, (
        "Should return an empty df when the role is invalid.\n\n" + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )


def test_empty_result_when_expression_with_column_of_strings() -> None:
    df = pd.DataFrame([["one", "two"]] * 2, columns=["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one*label_two", "label_three")
    assert df_result.empty, (
        "Should return an empty df when expression contain string column.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, "label_one+label_two", "label_three")
    assert df_result.empty, (
        "Should return an empty df when expression contain string column.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, "2*label_one", "label_three")
    assert df_result.empty, (
        "Should return an empty df when expression contain string column.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )
    df_result = add_virtual_column(df, "2+label_one", "label_three")
    assert df_result.empty, (
        "Should return an empty df when expression contain string column.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )


def test_not_empty_result_when_str_column_not_in_expression() -> None:
    df = pd.DataFrame([["one", 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([["one", 1, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "3*label_two", "label_three")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_not_empty_result_when_some_whitespaces_1() -> None:
    df = pd.DataFrame([["one", 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([["one", 1, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "   3 \n   *label_two\r\n\t", "label_three")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_not_empty_result_when_some_whitespaces_2() -> None:
    df = pd.DataFrame([["one", 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([["one", 1, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    role = """
    3
                *
                    label_two    """
    df_result = add_virtual_column(df, role, "label_three")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_not_empty_result_when_some_whitespaces_3() -> None:
    df = pd.DataFrame([["one", 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([["one", 1, 3]] * 2, columns=["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "3\n*\nlabel_two", "label_three")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_not_empty_result_when_capital_letters_in_new_column_name() -> None:
    df = pd.DataFrame([["one", 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([["one", 1, 3]] * 2, columns=["label_one", "label_two", "THREE"])
    df_result = add_virtual_column(df, "3*label_two", "THREE")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_not_empty_result_when_capital_letters_in_dataframe_column_name() -> None:
    df = pd.DataFrame([["one", 1]] * 2, columns=["label_ONE", "label_TWO"])
    df_expected = pd.DataFrame([["one", 1, 3]] * 2, columns=["label_ONE", "label_TWO", "label_three"])
    df_result = add_virtual_column(df, "3*label_TWO", "label_three")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*label_TWO.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_python_keyword_in_new_column_name() -> None:
    df = pd.DataFrame([["one", 1]] * 2, columns=["label_ONE", "label_TWO"])
    df_expected = pd.DataFrame([["one", 1, 3]] * 2, columns=["label_ONE", "label_TWO", "break"])
    df_result = add_virtual_column(df, "3*label_TWO", "break")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*label_TWO.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_python_keyword_in_role() -> None:
    df = pd.DataFrame([["one", 1]] * 2, columns=["label_ONE", "break"])
    df_expected = pd.DataFrame([["one", 1, 3]] * 2, columns=["label_ONE", "break", "label_two"])
    df_result = add_virtual_column(df, "3*break", "label_two")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*break.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_python_keyword_in_role_and_new_column() -> None:
    df = pd.DataFrame([[-1, 2]] * 2, columns=["not", "and"])
    df_expected = pd.DataFrame([[-1, 2, 1]] * 2, columns=["not", "and", "or"])
    df_result = add_virtual_column(df, "not + and", "or")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: not + and.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )


def test_overwriting_values_in_column() -> None:
    df = pd.DataFrame([["one", 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([["one", 3]] * 2, columns=["label_one", "label_two"])
    df_result = add_virtual_column(df, "3*label_two", "label_two")
    assert df_result.equals(df_expected), (
        "The function should calculate the value of the expression: 3*label_two.\n\n"
        + f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )
