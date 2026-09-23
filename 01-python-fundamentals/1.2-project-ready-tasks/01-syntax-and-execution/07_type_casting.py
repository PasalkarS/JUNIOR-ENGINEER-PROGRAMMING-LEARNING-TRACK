# 07 - Type Casting
# Converts between incompatible data types safely.

str_num = "100"
converted_int = int(str_num)
float_val = float(converted_int)
back_to_str = str(float_val)

print("Original str:", repr(str_num), type(str_num))
print("To int:", converted_int, type(converted_int))
print("To float:", float_val, type(float_val))
print("Back to str:", repr(back_to_str), type(back_to_str))
