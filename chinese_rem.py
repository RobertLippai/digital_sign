from modular_exp import modular_exp
from eucledian import extended_eucledian


def chinese_rem(c, m1_q, m2_p, d, m_n):
    c1 = modular_exp(c, (d % (m2_p - 1)), m2_p)
    c2 = modular_exp(c, (d % (m1_q - 1)), m1_q)

    g, y2, y1 = extended_eucledian(m2_p, m1_q)

    return ((c1 * y1 * m1_q) + (c2 * y2 * m2_p)) % m_n

