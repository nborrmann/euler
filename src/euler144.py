import math

x = 0
y = 10.1

m = (y - 1.4) / (x - -9.6)
c = 10.1


i = 0
while 1:
    x_new = (2 * m * c - math.sqrt(4 * m * m * c * c + 4 * (-m * m - 4) * (c * c - 100))) / (2 * (-m * m - 4))
    if math.fabs(x-x_new) < 0.000001:
        x_new = (2 * m * c + math.sqrt(4 * m * m * c * c + 4 * (-m * m - 4) * (c * c - 100))) / (2 * (-m * m - 4))

    x = x_new
    y = m * x + c

    if -0.01 <= x <= 0.01 and y > 0:
        print(i)
        break

    m_tangent = -4 * x / y
    m = (-m + 2 * m_tangent + m * m_tangent * m_tangent) / (2 * m * m_tangent - m_tangent * m_tangent + 1)
    c = y - m * x

    i += 1
    print("%04d: Hit ellipsis at %0.4f:%0.4f. Beam outgoing with y = %0.4f * x + %0.4f" % (i, x, y, m, c))

