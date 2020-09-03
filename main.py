import numpy as np
import scipy as sp
import scipy.stats as st
import matplotlib.pyplot as plt


    
if __name__ == "__main__":
    
    
    n_list = np.arange(1,101)  # the number of independent Gaussian rvs
    p_list = np.zeros(len(n_list))  # P(max_i X_i > sqrt(2*log(n)))
    
    for n in n_list:
        threshold = np.sqrt(2.1*np.log(n))
        N = 20000   # number of simulations
        max_x_list = np.zeros(N)
        for i in range(N):
            max_x_list[i] = np.max(np.random.normal(0,1,n))
        p_list[n-1] = sum(max_x_list <= threshold) / N
        
    plt.figure(1) 
    plt.plot(n_list, p_list)       
    plt.grid()
    plt.xlabel('n')
    plt.ylabel(r'$P(\max_i X_i \leq \sqrt{2.1 \log n})$')
    plt.title('Distribution of the maximum of n independent Gaussian random variables')
    plt.show() 
  
        
