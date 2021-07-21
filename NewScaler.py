import numpy as np

#Scaler
class NewScaler:
    # 평균, 표준편차 생성
    def __init__(self):
        self.mean_num = None
        self.std_num = None

    # 입력받은 배열로 평균, 표준편차 구하기
    def fit(self, arr):
        if arr is None:
            print("fit() missing 1 required positional argument: 'X'")

        total = 0
        n = 0
        
        for it in range(arr.size):
            num = arr.iat[it, 0]
            if num != 0 :
                total += num
                n += 1
        
        self.mean_num = total / n
        self.std_num = np.std(arr)

    # fit된 모델로 arr을 scale 적용
    def transform(self, arr):
        if arr is None:
            print("fit() missing 1 required positional argument: 'X'")

        return (arr - self.mean_num) / self.std_num      

    # fit + transform
    def fit_transform(self, arr):
        if arr is None:
            print("fit() missing 1 required positional argument: 'X'")

        total = 0
        n = 0
        
        for it in range(arr.size):
            num = arr.iat[it, 0]
            if num != 0 :
                total += num
                n += 1
        
        self.mean_num = total / n
        self.std_num = np.std(arr)

        return (arr - self.mean_num) / self.std_num  