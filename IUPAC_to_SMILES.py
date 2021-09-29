from urllib.request import urlopen
from urllib.parse import quote
import pandas as pd


def CIRconvert(ids):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles'
        ans = urlopen(url).read().decode('utf8')
        return ans
    except:
        return 'Did not work'

df = pd.read_excel('Data.xlsx')
identifiers = df["Molecule name"]
print(list(identifiers))

df['SMILES'] = [CIRconvert(ids) for ids in identifiers]
print(df.head)

df.to_excel("New_Data.xlsx")

