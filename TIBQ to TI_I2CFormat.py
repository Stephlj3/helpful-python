# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:53:17 2015

@author: Steph

Takes generated coefficient file from TIBQ.exe and outputs TI I2C format

This script intended for TLV320AIC32xx DAC PRB25 - generates Biquads B through F only
See pg.44-45 of Applications Resource Guide : http://www.ti.com/lit/ug/slau306a/slau306a.pdf

"lazy man's awk"

"""
import array

d = 5
j = 32 #left biquad 2 starts at register 32
k = 40 #right biquad 2 starts at register 40
a = s = 1
b = c = e = f =  0
t = ['w 30 ']

with open('Generated Coefficients_2.txt', 'rb') as in_file:  #Input file
    with open('Biquad_TI_I2C_Format.txt', 'wb') as out_file:  #output file
        out_file.write('#WARNING: This code has been generated automatically. Edit at your own risk\n\n')

        for line in in_file:
                out_file.write('#%s' % (line))

                if 'Filter %d BQ' % (a) in line:
                    out_file.write('#-----------------------------------------------------------------\n')
                    out_file.write('#Set Left Biquad %d (start at Register %d)\n' % (a,j))
                    t.append('%02x ' % (j))
                    a += 1
                    j += 20
                    out_file.write('#select pg. 44 - Left DAC\n')
                    out_file.write('w 30 00 2C\n\n')          
                    
                elif '0x' in line:
                    b += 1
                    c = b % 5
                    for d in xrange(2,8):
                            t.append('%s' % (line[d]))
                            e += 1
                            f += 1
                            if e % 2 == 0 :
                                    t.append(' ')
                                    if f % 3 == 0 and c != 0:
                                            t.append('00 ')

                    
                    if '0x' in line and c == 0:

                            #copy into left dac
                            u = "".join(t)
                            out_file.write('\n%s\n\n' % (u))

                            #copy into right dac
                            out_file.write('#Set Right Biquad %d (start at Register %d)\n' % (s,k))
                            t.pop(1)
                            t.insert(1, '%02x ' % (k))
                            s += 1
                            k += 20
                            out_file.write('#select pg. 45 - Right DAC\n')
                            out_file.write('w 30 00 2D\n')
                            u = "".join(t)
                            out_file.write('\n%s\n\n' % (u))

                            #reset for next biquad
                            t = ['w 30 ']
                            
