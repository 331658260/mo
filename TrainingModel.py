#导⼊相关包
import pickle
import warnings
warnings.filterwarnings('ignore')
import pandas as pd

# 拆分预测数据和训练数据
from sklearn.model_selection import train_test_split

# 模型
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from lightgbm import LGBMRegressor
from mlxtend.regressor import StackingCVRegressor

#交叉验证
from sklearn.model_selection import KFold


#模型评估
from sklearn import metrics



# 导⼊数据
train= pd.read_csv('./data/建设用地处理后数据.csv',encoding='gbk')


X = train.drop(['样点地价'], axis = 1)
y = train['样点地价']

# 拆分为训练和测试数据
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

# 使用 stacking 堆栈模型

reg_1 = RandomForestRegressor()
reg_3 = LGBMRegressor()
reg_4 = GradientBoostingRegressor()
reg_5 = ExtraTreesRegressor()

models = [
    (reg_1),
    (reg_3),
    (reg_4),
    (reg_5),
]

# 创建stacking模型
reg = StackingCVRegressor(regressors=models, meta_regressor=reg_4, cv=KFold(n_splits=5), verbose=0, random_state=42,
                          n_jobs=-1)
reg.fit(X_train, y_train)
pickle.dump(reg,open('model.pkl','wb'))

y_test_pred = reg.predict(X_test)#输入预测集获得预测值
R2 = metrics.r2_score(y_test, y_test_pred)

print("模型保存完毕,模型分数为：",R2)