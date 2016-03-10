import numpy as np

class LSRegression:
    '''
    Polynomial regression by solving the matrix equation 
    '''
    def __init__(self):
        '''
        Initialization for parameters:
        lamda=0, degree=1
        '''
        self.lamda = 0
        self.degree = 1
        self.theta = np.zeros((2,1))
        
    def set_lamda(self,lamda):
        '''
        set l2_penalty
        @param lamda: l2_penalty
        '''
        self.lamda=lamda
        
    def polynomial_fit(self,x,y,deg):
        '''
        curve fitting for the given data
        @param x: input vector
        @param y: target vector
        @param deg: ploynimial degree
        
        @return theta: model parameters
        @return loss: final calue of J(x,y,theta)
        
        This function evaluates: 
            minimize J(x,y,theta) = 1/(2*n)(sum(theta*x-y)^2 + sum(lamda*theta^2))
            by solving the matrix equation
        '''
        self.degree = deg
        loss = 0
        feature_matrix = np.zeros((len(x),deg+1))
        for i in np.arange(0,len(x)):
            for j in np.arange(0,deg):
                feature_matrix[i][j] = x[i]**j
        self.theta = np.zeros((deg+1,1))
        A = feature_matrix
        B = np.dot(A.T,A)
        I = np.dot(self.lamda, np.identity(B.shape[0]))
        self.theta = np.dot(np.dot(np.linalg.pinv(B+I),A.T),y)
        C = np.dot(A,self.theta)-y
        loss = np.dot(C.T,C)
        
        return self.theta,loss
    
    def prediction(self, x):
        '''
        Predict putput for unknown input data
        @param x: input data
        
        @return y: prediction output
        '''
        y = np.zeros((len(x),1))
        for i in np.arange(0,len(x)):
            for j in np.arange(0,self.degree+1):
                y[i] += self.theta[j]*(x[i]**j)
        return y