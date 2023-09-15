"""
JISの定義に基づいて放射照度を求める

input :眼底画像 
output :テンプレート画像
"""
import math
coneHeight = 10
coneradius = 0.5
radientEnergy = 2.5
coneAngle = 2 * math.atan(coneradius/coneHeight)

omega = 4 * math.pi *(math.sin(coneAngle/4))*(math.sin(coneAngle/4))

rentalArea = 1.7 *1.7 * omega
cornealArea = 0.3*0.3*math.pi



rentalFlux = (radientEnergy / rentalArea) *0.5
cornealFlux =(radientEnergy/cornealArea)

print(rentalArea)
print(cornealArea)
print("rentalFlux")
print(rentalFlux)
print("cornealFlux")
print(cornealFlux)

time =10
icnrp = 1.8 *(time**(-3/4))

print(icnrp)
