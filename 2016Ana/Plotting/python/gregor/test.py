#!/usr/bin/env python

import ROOT

c = ROOT.TCanvas( "","", 800, 800)
c.Print("test.pdf")
