   PassengerId  Survived  Pclass      Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3  jagadeep    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1    ananya  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3    akalya  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1      ammu  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3     vijay    male   NaN      0      0            373450   8.0500   NaN        S
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  10 non-null     int64
 1   Survived     10 non-null     int64
 2   Pclass       10 non-null     int64
 3   Name         10 non-null     object
 4   Sex          10 non-null     object
 5   Age          8 non-null      float64
 6   SibSp        10 non-null     int64
 7   Parch        10 non-null     int64
 8   Ticket       10 non-null     object
 9   Fare         10 non-null     float64
 10  Cabin        4 non-null      object
 11  Embarked     10 non-null     object
dtypes: float64(2), int64(5), object(5)
memory usage: 1.1+ KB
None
       PassengerId   Survived     Pclass        Age      SibSp      Parch       Fare
count     10.00000  10.000000  10.000000   8.000000  10.000000  10.000000  10.000000
mean       5.50000   0.500000   2.300000  27.250000   0.700000   0.300000  27.844990
std        3.02765   0.527046   0.948683  15.736672   0.948683   0.674949  23.018405
min        1.00000   0.000000   1.000000   2.000000   0.000000   0.000000   7.250000
25%        3.25000   0.000000   1.250000  20.000000   0.000000   0.000000   8.820825
50%        5.50000   0.500000   3.000000  26.500000   0.500000   0.000000  18.887500
75%        7.75000   1.000000   3.000000  35.750000   1.000000   0.000000  46.414575
max       10.00000   1.000000   3.000000  54.000000   3.000000   2.000000  71.283300
PassengerId    0
Survived       0
Pclass         0
Name           0
Sex            0
Age            2
SibSp          0
Parch          0
Ticket         0
Fare           0
Cabin          6
Embarked       0
dtype: int64
D:\AI &ML internship\task1\data.py:10: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  df['Age'].fillna(df['Age'].median(), inplace=True)
   PassengerId  Survived  Pclass      Name  Sex       Age  SibSp  Parch            Ticket      Fare  Embarked_Q  Embarked_S
0            1         0       3  jagadeep    0 -0.367381      1      0         A/5 21171 -0.894718       False        True
1            2         1       1    ananya    1  0.785187      1      0          PC 17599  1.887112       False       False
2            3         1       3    akalya    1 -0.079239      0      0  STON/O2. 3101282 -0.865394       False        True
3            4         1       1      ammu    1  0.569081      1      0            113803  1.097166       False        True
4            5         0       3     vijay    0 -0.043221      0      0            373450 -0.859964       False        True
Final shape after cleaning: (8, 12)
