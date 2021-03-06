import numpy as np
import math

def binomial_model(S0,r, K,sd,expiration):
    s=10000
    N=expiration*s
    u=math.exp((sd/s)*math.sqrt(1/(365*s)))
    r=r/(N*100)
    
    """
    N = number of binomial iterations
    S0 = initial stock price
    u = factor change of upstate
    r = risk free interest rate per annum
    K = strike price
    sd=daily standard deviation
    s=iterations per day
    expiration=bds until expiration
    """
    
    d = 1 / u
    p = (1 + r - d) / (u - d)
    q = 1 - p
    
    stock = np.zeros([N + 1, N + 1])
    for i in range(N + 1):
        for j in range(i + 1):
            stock[j, i] = S0 * (u ** (i - j)) * (d ** j)

    option = np.zeros([N + 1, N + 1])
    option[:, N] = np.maximum(np.zeros(N + 1), (stock[:, N] - K))
    
    for i in range(N - 1, -1, -1):
        for j in range(0, i + 1):
            option[j, i] = (
                1 / (1 + r) * (p * option[j, i + 1] + q * option[j + 1, i + 1])
                )
            
    return option

if __name__ == "__main__":
    op_price = binomial_model(267.99, 0.23375,205,5.578001895153531,5)
    print(op_price[1,1])
