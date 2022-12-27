# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

# =============================================================================

# Решение:

num_1 = input("Enter a real number: ")
num_2 = input("Enter the required accuracy '0.0001': ")


def required_accuracy(n: str, accuracy: str) -> float:
    from decimal import Decimal
    result = Decimal(n)
    result = result.quantize(Decimal(accuracy))

    return result


new_num_1 = required_accuracy(num_1, num_2)

print(new_num_1)


# =============================================================================
