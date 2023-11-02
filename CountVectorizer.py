import math


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


class TfidfTransformer:

    def __init__(self):
        pass

    def tf_transform(self, count_matrix: list) -> list:
        """Returns term's frequency in document"""
        transformed_matrix = []
        for document in count_matrix:
            s = sum(document)
            tmp = []
            for word in document:
                tmp.append(word / s)
            transformed_matrix.append(tmp)
        return transformed_matrix

    def idf_transform(self, count_matrix: list) -> list:
        """Returns inverse  document frequency"""
        c_matrix_len = len(count_matrix)
        document_len = len(count_matrix[0])
        idf = []
        for i in range(document_len):
            s = 0
            for j in range(c_matrix_len):
                if count_matrix[j][i] > 0:
                    s += 1
            idf.append(math.log((c_matrix_len + 1) / (s + 1)) + 1)
        return idf

    def fit_transform(self, count_matrix: list) -> list:
        """Transforms data"""
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        result = []
        for i in range(len(tf)):
            tmp = []
            for j in range(len(idf)):
                tmp.append(idf[j] * tf[i][j])
            result.append(tmp)
        return result


class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        super().__init__()
        self.tf_idf_transformer = TfidfTransformer()

    def fit_transform(self, data: list) -> list:
        """Learn vocabulary and idf, return document-term matrix"""
        count_matrix = super().fit_transform(data)
        return self.tf_idf_transformer.fit_transform(count_matrix)
