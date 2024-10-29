# Bit Manipulation

Processors can efficiently perform different manipulations on the bits of a number.

## Binary operations
- **AND**: a bit is 1 in the result if and only if both the corresponding bits of the operands is 1

| a | b | a&b |
|---|---| --- |
| 0 | 0 | 0   |
| 0 | 1 | 0   |
| 1 | 0 | 0   | 
| 1 | 1 | 1   |

- **OR**: a bit is 1 in the result if and only if at least one of the corresponding bits of the operands is 1

| a | b | a\|b |
|---|---| --- |
| 0 | 0 | 0   |
| 0 | 1 | 1   |
| 1 | 0 | 1   | 
| 1 | 1 | 1   |

- **XOR**: a bit is 1 in the result if and only if exactly one of the corresponding bits of the operands is 1 

| a | b | a^b |
|---|---| --- |
| 0 | 0 | 0   |
| 0 | 1 | 1   |
| 1 | 0 | 1   |
| 1 | 1 | 0   |


## Unary operators
- Bitwise negation: reverses all the bits of a number.

| n        | ~n       |
| -------- | -------- |
| 10011001 | 01100110 |
| 11001101 | 00110010 |

Generally, signed and unsigned number are represented with the Two's Complement method.  That is, if $n$ is some number, then $\sim n+1$ is the binary representation of $-n$. 