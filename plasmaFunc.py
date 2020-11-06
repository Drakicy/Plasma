def plasmaFunc(arg, intervals_eps = 1e-3):
    import numpy as np
    
    sign = np.sign(arg)
    abs_arg = np.abs(arg)
    
    def func(x, singularity):
        if x == singularity:
            return 2 * singularity * np.e**(-singularity**2)
        else:
            return (np.e**(-x**2) - np.e**(-singularity**2)) / (x - singularity)
    
    if abs_arg > np.e:
        b = np.sqrt(np.log(1 / intervals_eps))
        a = -np.sqrt(np.log(1 / intervals_eps))
        n = 2**(np.log10(1 / intervals_eps))
    else:
        b = 1 / intervals_eps
        a = -1 / intervals_eps
        n = np.e / intervals_eps

    step = (b - a) / n
    points = np.arange(a + step / 2, b, step)
    I = step * np.sum([func(point, abs_arg) for point in points])
    
    return sign * I / (np.sqrt(np.pi))