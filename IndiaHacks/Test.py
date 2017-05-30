import pandas as pd
class Test:
	def run(self,path):
		data = pd.read_csv(path)
		print(data.head())
if __name__ == "__main__":
	path = "D:\\Vishal\\HackerEarth\\IndiaHacks\\dataset\\train.csv"
	obj = Test()
	obj.run(path)
	