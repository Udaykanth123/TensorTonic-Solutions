import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Write code here
    curr_sum = 0
    for i in range(len(p)):
        if p[i]!=0:
            curr_sum += p[i]*np.log(p[i]/(q[i]+eps))
            
    return curr_sum