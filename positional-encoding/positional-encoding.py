import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    PE = np.zeros((seq_len,d_model))
    for i in range(seq_len):
        for j in range(d_model//2):
                PE[i][2*j] = np.sin(i/(np.power(base,((2*j)/d_model))))
                PE[i][2*j+1] = np.cos(i/(np.power(base,((2*j)/d_model))))
        if d_model%2!=0:
            j = d_model //2
            PE[i][2*j] = np.sin(i/(np.power(base,((2*j)/d_model))))
    return PE