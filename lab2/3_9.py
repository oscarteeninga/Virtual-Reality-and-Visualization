pd = reader.PointData
print(pd.keys())
print(pd['pres'].GetNumberOfComponents())
print(pd['pres'].GetRange())
print(pd['v'].GetNumberOfComponents())

for ai in pd.values():
    print(ai.GetName(), ai.GetNumberOfComponents(), end=' ')
    for i in range(ai.GetNumberOfComponents()):
        print(ai.GetRange(i), end=' ')
    print()