import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here
    scores_mask = scores.copy()
    dim = len(scores.shape)
    if dim == 2:
        m,n  = scores.shape
        for i in range(m):
            for j in range(i+1,n):
                scores_mask[i][j] = mask_value
        return scores_mask
    elif dim == 3:
        m,n,p = scores.shape
        for i in range(m):
            for j in range(n):
                for k in range(j+1,p):
                    scores_mask[i][j][k] = mask_value
        return scores_mask
    elif dim == 4:
        m,n,o,p = scores.shape
        for i in range(m):
            for j in range(n):
                for l in range(o):
                    for k in range(l+1,p):
                        scores_mask[i][j][l][k] = mask_value
        return scores_mask
        
        