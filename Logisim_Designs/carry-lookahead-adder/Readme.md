# CARRY LOOKAHEAD ADDER

The idea is to optimize a simple pipelined adder, which main probleme is the
propagation time of the carry between each adder of each bit of the addition.

To reduce that propagation time, we need to calculate each carry faster.
To do so, instead of calculating the carry in each full adder, we only calculate
if the addition of 2 bits propagate and generate a carry.

    So here a full adder return S 'Solution', P 'Propagate Carry' and G 'Generate Carry'.

To calculate the Carry of each adder i we only need to do so:
    Here '+' is a logical Or and '.' a logical And.

    C(i + 1) = G(i) + P(i) . C(i)

    Which lead to this for a 4bits adder:

    C(0) is given.
    C(1) = G(0) + P(0) . C(0)
    C(2) = G(1) + P(1) . C(1)
    C(3) = G(2) + P(2) . C(2)
    C(4) = G(3) + P(3) . C(3)

    Which can be reduce so we do not only need the carry C0 to compute each carry of
    each adder.

    S0 = A0 xor B0 xor C0
    S1 = A1 xor B1 xor C1
    S2 = A2 xor B2 xor C2
    S3 = A3 xor B3 xor C3

With implementation the propagation time of the carry is reduce but can still
be pretty big with a 64 bits adder for example.
