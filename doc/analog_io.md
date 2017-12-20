# Analog GPIO

**Note:** Testing was done with an ADS1115 and MCP4725. The results reported include the errors of the ADS1115 (negligible compared to the errors of the ESP-32).

## Digital-to-Analog Converter (DAC)

The DAC reference voltage equals the supply, V<sub>DD</sub> (nominally 3.3V). The code below sets the DAC1 output voltage V<sub>out</sub> to 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = code*V<sub>DD</sub>/255

```python
from board import DAC1
from machine import Pin, DAC

dac1 = DAC(Pin(DAC1))

code = 100
# perform conversion
dac1.write(code)
```

![DAC output voltage versus input code (0 ... 255)](adc/esp32_dac.png)

## Analog-to-Digital Converter (ADC)

The ESP-32 contains two 12-Bit ADCs (nominal, the actual performance is much lower, see measurement results below), one of which is available to the user.

The ADC output code for input V<sub>in</sub> equals

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;code = V<sub>in</sub>/V<sub>ref</sub> * 4095

The `attn(arg)` function sets the reference V<sub>ref</sub> (see example below). Valid arguments and the corresponding approximate values of V<sub>ref</sub> are:

arg | V<sub>ref</sub>
------| ---------------
ADC.ATTN_0DB   | 1.1 V
ADC.ATTN_2_5DB | 1.3 V
ADC.ATTN_6DB   | 1.8 V
ADC.ATTN_11DB  | 3.2 V

**Note:** The ADC characteristics vary substantially between parts and suffer from a large offset and poor linearity. See measurement results below.

```python
from board import ADC0
from machine import Pin, ADC

adc0 = ADC(Pin(ADC0))

# set full-scale range
adc0.atten(ADC.ATTN_0DB)

# perform conversion
code = adc0.read()
```

![ADC output code versus input voltage](adc/esp32_adc_vin.png)

![ADC offset](adc/esp32_adc_vin_offset.png)

![ADC INL for 0 dB attenuation](adc/esp32_adc_inl_0dB.png)

![ADC INL for 2.5 dB attenuation](adc/esp32_adc_inl_2.5dB.png)

![ADC INL for 6 dB attenuation](adc/esp32_adc_inl_6dB.png)

![ADC INL for 11 dB attenuation](adc/esp32_adc_inl_11dB.png)
