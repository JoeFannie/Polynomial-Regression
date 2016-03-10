# Polynomial-Regression  
polynomial regression for single variable  
I use 2 methods.   
1. Gradient descent   
  The code includes main.py and Regression.py.   
2. Directly solving the matrix equation by least quare   
  The code includes LSmain.py and LSRegression.py.   
3. I also use functions in lib to run the expriment. The code is Polyfit&&Lasso.py.   

Since I use small group of data, so the second method is better and I put my results here   
1. Degree=3 Sample=10 Lamda=0   
![image](https://github.com/JoeFannie/Polynomial-Regression/edit/master/results/ls3d10s.png)   
2. Degree=9 Sample=10 Lamda=0   
![image](https://github.com/JoeFannie/Polynomial-Regression/edit/master/results/ls9d10s.png)   
3. Degree=9 Sample=15 Lamda=0   
![image](https://github.com/JoeFannie/Polynomial-Regression/edit/master/results/ls9d15s.png)   
4. Degree=9 Sample=100 Lamda=0   
![image](https://github.com/JoeFannie/Polynomial-Regression/edit/master/results/ls9d100s.png)   
5. Degree=9 Sample=10 Lamda=exp(-15)   
![image](https://github.com/JoeFannie/Polynomial-Regression/edit/master/results/ls9d10swithRe.png)   
   
You can see results for other methods in the /results folder.\n
