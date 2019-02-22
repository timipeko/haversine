from wrapper import wrapper 

w = wrapper.GmapsWrapper()

london = (51.38494009999999, -0.3514683)
paris = (48.856614,2.3522219)

def test_kilometers():
    assert w.calculate_distance(london, paris) == "343.55 km"
