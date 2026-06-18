def convert(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return x

data =dict(convert(x) for x in input().split())
print(data)