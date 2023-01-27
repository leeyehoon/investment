import pyupbit

access = "C8ZdPB9QLYxCAZ2RXiMeTuVBG1p0NqOVyvVDswTq"
secret = "mU2jrVX1KtizqfXxxJ4x0KFZ1S5RKxdAD5qU2QC0"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회