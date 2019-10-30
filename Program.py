import QuantLib as ql
today = ql.Date(30, 10, 2019)
ql.Settings.instance().evaluationDate = today  
settlementDate = ql.TARGET().advance(today, ql.Period(2, ql.Days))

rts = [0.03145, 0.03145, 0.0278373626373627, 0.0253076923076923, 0.0249373626373629]
dts = [settlementDate, ql.Date(1,2,2020), ql.Date(1,5,2020), ql.Date(1,8,2020), ql.Date(1,11,2020)]
c = ql.ForwardCurve(dts, rts, ql.Actual360(), ql.NullCalendar(), ql.BackwardFlat())
df = [c.discount(d) for d in dts]
print(df)

for i in range(len(rts) - 1):
    r_simple = ql.InterestRate(rts[i + 1], ql.Actual360(), ql.Simple, ql.Once)
    t = ql.Actual360().yearFraction(dts[i], dts[i + 1])
    r_continuous = r_simple.equivalentRate(ql.Continuous, ql.NoFrequency, t)
    rts[i + 1] = r_continuous.rate()
    
# set rate for the first node
rts[0] = rts[1]
c = ql.ForwardCurve(dts, rts, ql.Actual360(), ql.NullCalendar(), ql.BackwardFlat())
df = [c.discount(d) for d in dts]
print(df)
