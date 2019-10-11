'''
#creating linear regression using skikit learn 

from sklearn.linear_model import LinearRegression 
lm=LinearRegression()
X = df[['highway-mpg']]
Y = df['price']
lm.fit(X, Y)
Yhat=lm.predict(X)

'''
''' 
#creating a regression plot it gives the line made 

import eaborn as sns
sns.regplot(x='highway-mpg',y='price',data=df)
plt.ylim(0,)


#creating residual plot (diferance between predicted and actual value) wrt to x or value at x axis ..uniform distribution means our rgresion is good
sns.residplot(df['highway-mpg'],df['price'])

'''
'''
#creating distribution plot (gives direct picture of actuall value and pridiction value in graphical way)
import seaborn as sns

axl=sns.distplot(df['price'],hist=False,color="r",label="actual values")
sns.distplot(Yhat,hist=False,color="b",label="fited value",ax=axl)
'''
'''
#creating polynomial regression
import npm as np
f=np.polyfit(x,y,3)
n=np.polydl(f)
print(n)
#this cannnot do multivariest polynomial regression for this implement follaowing code


from sklearn.preprocessing import PolynomialFeatures
pr=PolynomialFeatures(degree=2)
x_polly=pr.fit_transform(x[['horse-power','curb-weight']],include_bias=False)

'''
'''

#creating pipeline reduces both efforts of normalization and polynomalization directly after we can do linear regression
import sklearn

input=[('scale',StandardScaler()),('polynomial',PolynomialFeatures()] #also add other features you need to add.
pipe=pipeline(input)
#so does it continue most important is it eas the code

'''
'''
#mostly model is evaluted by mse i.e mean square and second is r square 
#r sqare implementation is.

lm = LinearRegression()
lm.score(X,y)
X = df[['highway-mpg']]
Y = df['price']
lm.fit(X, Y)
out=lm.score(X,y)

'''