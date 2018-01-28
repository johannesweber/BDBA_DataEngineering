from python.BokehHelper import BokehPlotter
from python.DBHelper import DBHelper

plotter = BokehPlotter()
db = DBHelper("bdba")
count = 0
latList = []
lonList = []

results = db.selectAllEntriesWhere(table_name="service_request", key="borough", value="BROOKLYN")

for result in results:
    latList.append(result["latitude"])
    lonList.append(result["longitude"])
    count += 1
print(count)

plotter.plotgeo(latList=latList, lonList=lonList, notebook=False)