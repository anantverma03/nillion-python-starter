from nada_dsl import *

def nada_main():
    # Define two parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Inputs from each party
    input1 = Input(name="input1", party=party1)
    input2 = Input(name="input2", party=party2)

    # Secure integers for each party's input
    my_int1 = SecretInteger(input1)
    my_int2 = SecretInteger(input2)

    # Secure comparisons and conditional assignments
    is_smaller_or_equal = my_int1 <= my_int2
    min_value = IfElse(is_smaller_or_equal, my_int1, my_int2)

    # Outputs the minimum value
    return [Output(min_value, "min_value_output", party1)]