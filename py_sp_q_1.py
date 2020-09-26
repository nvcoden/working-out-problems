import sys
from io import StringIO
sys.stdin = StringIO('''4
1001
Sonal Sharma
Laptop
Yashwin, Hinjewadi, Mumbai, Maharashtra - 411058
1002
Ananya Tiwari
Desktop
Tinsel Town, Ahmedabad, Gujrat - 400150
1003
Raghav Rijija
Laptop
airport road, Kochi, Kerala - 682001
1004
Arun Singh
Desktop
sadar bazaar, Hinjewadi, Pune, Maharashtra - 411057
Laptop
Mumbai
''')

class Asset:
    def __init__(self,a,b,c,d):
        self.asset_id = a
        self.asset_holder_name  = b
        self.asset_type = c
        self.asset_location = d

class AssetManager:
    def __init__(self, e, f):
        self.asset_manager_name = e
        self.asset_list = f
    
    def findAssetIdWithNameBasedOnAssetType(self, typ):
        funlist = []
        for i in self.asset_list:
            if typ.lower() == i.asset_type.lower():
                funlist.append([i.asset_id, i.asset_holder_name])
        return funlist

    def countAssetsBasedOnLocation(self, loc):
        count = 0
        for i in self.asset_list:
            if loc.lower() in i.asset_location.lower().strip():
                count+=1
        return count


n = int(input())
assetlist = []
for i in range(n):
    a = int(input())
    b = input()
    c = input()
    d = input()
    assetlist.append(Asset(a, b, c, d))
obj = AssetManager("Manager_name", assetlist)

findtype = input()
ans1 = obj.findAssetIdWithNameBasedOnAssetType(findtype)
if ans1 == []:
    print("No asset found with the given asset type")
else:
    for i in ans1:
        ran_str = ""
        for j in i:
            ran_str+=str(j)+" "
        print(ran_str)

findlocation = input()
ans2 = obj.countAssetsBasedOnLocation(findlocation)
if ans2 == 0:
    print("No asset found in the given location")
else:
    print(ans2)