import os
import pickle
import numpy as np
class SmartphonePricePredict:

    def __init__(self, model_name) -> None:
        self.model = self.load_model(model_name)
        self.config_label = self.load_config_label()

    def load_model(self, model_name="SoftmaxRegression"):
        """
        model_name:
            DecisionTree
            SoftmaxRegression

        """
        model = pickle.load(open(os.path.join("weights", model_name+".pkl"), "rb"))
        return model

    def load_config_label(self):
        labels = {
            0: "low",
            1: "medium",
            2: "high",
            3: "very high"
        }
        return labels

    def predict(self, data):
        data = self.process(data)
        prediction = self.model.predict(data)
        return self.config_label[prediction[0]]

    def process(self, data):
        ldata = []
        for k, v in dict(data).items():
            ldata.append(v)


   

        data = np.asarray(ldata).reshape(-1, len(ldata))
        return data
