class CountVectorizer:

    def __init__(self):
        self.__features: dict = {}
        self.__count_matrix: list = []

    def fit_transform(self, raw_data) -> list:
        """Creates a matrix of token counts from text"""
        for element in raw_data:
            line = element.lower().split(' ')
            self.__features = {k: 0 for k in self.__features}
            for word in line:
                if word in self.__features:
                    self.__features[word] += 1
                else:
                    self.__features[word] = 1
            self.__count_matrix.append([v for v in self.__features.values()])

        n = len(self.__count_matrix[-1])
        for element in self.__count_matrix:
            if len(element) < n:
                element.extend([0] * (n - len(element)))

        return self.__count_matrix

    def get_feature_names(self) -> list:
        """Returns features' names"""
        return [k for k in self.__features]
